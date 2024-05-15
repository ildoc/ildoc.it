---
title: "A Kubernetes journey - Parte 1: il setup"
date: 2024-05-13 14:28:00
tags: kubernetes homelab ansible
media_subpath: /assets/img/posts/2024
---

Come anticipato in fondo al post sull'update dell [Homelab 2024]({% post_url 2024/2024-03-15-homelab-2024%}), il prossimo step è provare a sporcarsi le mani con Kubernetes.

Non ci avevo mai avuto a che fare, ma sul cliente per cui lavoro lo utilizziamo per deployarci i progetti che sviluppiamo e quindi per forza di cose ho cominciato a girarci un po'.

E ho scoperto che il mondo DEVOPS mi affascina molto, da qui la decisione di imparare Kubernetes.

Gli obbiettivi che mi piacerebbe provare a raggiungere sono:
- creare un cluster con più nodi
- avere un'infrastruttura facilmente replicabile
- avere tutte le configurazioni versionate
- ottenere una gestione dichiarativa di settings e deploy
- rendere il tutto facilmente scalabile
- riuscire a migrare su k8s la maggior parte dei servizi che attualmente faccio girare su varie vm e lxc con docker compose

Sarà tosta, ma è un gioco, un hobby, e nel frattempo imparerò anche un sacco di cose.

## L'hardware

Non c'è, o meglio non dedicato.

L'idea è quella di usare il server che ho attualmente in uso per fare prove e prendere un po' la mano con il processo e i vari tool, dopodichè un domani migrerò (se possibile) su dell'hardware apposta, oppure reinstallerò da zero il tutto.

Quindi per cominciare ho creato 3 vm su Proxmox con l'installazione minimale di Ubuntu 24.04, dandogli 8GiB di ram e 4CPU che saranno i tre nodi del cluster.

Per comodità ne ho creata anche una quarta con mooolte meno risorse che utilizzerò come ambiente di sviluppo per controllare il cluster in modo da potermici collegare semplicemente in ssh da pc diversi senza dover replicare l'ambiente su ciascuno di questi.

In ultimo per tutte e 4 le vm ho assegnato uno static lease dal DHCP del mio PiHole, in modo da poterle raggiungere agli ip scelti da me.


## Il setup 

### 1. l'ambiente di sviluppo

Prima di tutto ho installato `zsh` e `ohmyzsh` perchè è di una comodità assurda e dà anche un pizzico di colore alla shell, che visivamente aiuta molto.

```bash
sudo apt update
sudo apt install zsh curl
chsh -s /bin/zsh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

dopodichè ho clonato il progetto [k3s-ansible di TechnoTim](https://github.com/techno-tim/k3s-ansible)

```bash
sudo apt install git
git clone https://github.com/techno-tim/k3s-ansible.git
```

Questo progetto si avvale di [Ansible](https://www.ansible.com/) che è un tool fighissimo per automatizzare deploy, configurazioni, installazioni ecc. in maniera agentless, cioè senza la necessità di installare nulla sulla macchina di destinazione e idempotente, cioè che gli script possono essere applicati più volte senza che il risultato cambi da quello della prima esecuzione.

In pratica si definisce una lista di host detta "Inventory" e si definiscono delle serie di task organizzati in "Playbook", dopodichè all'avvio dello script tutti i task vengono applicati a tutti gli host dell'inventory semplicemente tramite connessione in ssh.

Questo è molto comodo per gestire parallelamente più macchine in maniera ripetibile e controllata, esattamente come il repository appena scaricato.


### 2. il progetto ansible

Il progetto ansible di TechnoTim porta ad avere un cluster k3s in high availability con etcd come database e con un load balancer già configurato, quindi un'ottima situazione di partenza.

K3s è una distribuzione più snella di Kubernetes adatta a girare su hardware meno performante, quindi esattamente il mio caso.

L'installazione in high availability (HA) implica il fatto di avere un minimo di 3 nodi che fanno da server e un minimo di 0 nodi che fanno da agent, quindi esattamente il mio caso. In questo modo anche se un nodo muore, gli altri due garantiscono che il cluster continui a funzionare senza interruzioni, ottimo per avere ridondanza e per semplificare update.

In realtà questo è un po' inutile nel mio caso, perchè comunque si parla di tre virtual hostate sullo stesso nodo di Proxmox, quindi se casca il server casca tutto, però mi interessava approfondire l'argomento, che nella fantasia magari un domani potrei avere più server.

Etcd a quanto ho capito è abbastanza una novità, e si tratta di un database key-value per i settings e le configurazioni di Kubernetes che viene distribuito sui vari nodi e permette quindi di evitare di utilizzare un sql esterno al cluster, come invece avveniva prima della sua introduzione. Comodo e pratico.

Infine il load balancer (MetalLB) serve a fare da ponte tra il dns e il proxy per raggiungere dall'esterno i servizi hostati da Kubernetes, perchè gli ip dei pod interni alla sottorete vengono assegnati a caso.

Dunque, per prima cosa ho installato Ansible con le sue dipendenze.

Ansible è un software Python installabile da `pip`, ma dall'introduzione della controversa [PEP-668](https://peps.python.org/pep-0668/), sembra che il metodo preferito sia utilizzare `pipx`, che in pratica è un wrapper di `pip` che gestisce automagicamente anche i virtualenv.

E `pipx` sia:

```bash
sudo apt install pipx
pipx install --include-deps ansible
pipx ensurepath
```

a questo punto nei requisiti del readme del progetto c'è scritto che è necessario anche il pacchetto `netaddr`, che quindi bisogna aggiungere al venv di ansible creato da pipx con

```bash
pipx inject ansible netaddr
```

E così Ansible è pronto, ora c'è da configurare una chiave ssh e pusharla sulle tre virtual in modo da potersi loggare in ssh senza che sia necessario inserire sempre la password, in questo modo il lavoro di ansible è più semplice.

```bash
ssh-keygen
```

e poi 

```bash
ssh-copy-id filippo@192.168.0.180
ssh-copy-id filippo@192.168.0.181
ssh-copy-id filippo@192.168.0.182
```

La cosa figa è che finora sulle tre macchine non ci ho mai messo piede, tutto il setup di k3s viene fatto da fuori.

Ora, venendo al progetto di TechnoTim, bisogna copiare la folder `/inventory/sample` e incollarla in `/inventory/my-cluster`, dopodichè bisogna andare a specificare l'ip delle macchine su cui si vuole installare il tutto nel file dell'inventory `/inventory/my-cluster/hosts.ini`

Io qui ho aggiunto i tre ip sotto il gruppo `[master]` lasciando invece vuoto il gruppo `[node]`

```ini
[master]
192.168.0.180
192.168.0.181
192.168.0.182

[node]

# only required if proxmox_lxc_configure: true
# must contain all proxmox instances that have a master or worker node
[proxmox]
# 192.168.30.43

[k3s_cluster:children]
master
node
```

dopodichè la ciccia vera sta tutta nel file `/inventory/my-cluster/group_vars/all.yml`.

Il file è molto grande, ma girando un po' nel progetto mi sono reso conto che alla fine le configurazioni da toccare sono poche:

```yaml
# l'utente che ansible usa sulle macchine
ansible_user: filippo

# la timezone da utilizzare
system_timezone: "Europe/Rome"

# interfaccia di rete usata da flannel
flannel_iface: "ens18"

# ip virtuale configurato su ciascun master
apiserver_endpoint: "192.168.0.222"

# il token usato dai master
k3s_token: "<inserire-token-super-segretissimo>"

# range di ip per il load balancer
metal_lb_ip_range: "192.168.0.80-192.168.0.90"
```

un utente con una pull request ha aggiunto un sacco di settings per calico e cilium (che non so bene cosa siano) che aggiungono molto "rumore" nello yaml di configurazioni, ma se uno lascia le cose di default basta modificare proprio poco.

Una cosa che mi ha dato problemi e ci ho messo un po' a capire è stato il setting `flannel_iface` che di default era `eth0`, che però sulle mie virtual si chiama (non so perchè) `ens18`, e una volta scoperto e sistemato il setting poi lo script è andato senza più problemi.

Per controllare il nome della propria interfaccia basta scrivere

```bash
ip link
```

L'altra cosa che ho fatto è stato andare sul DHCP di PiHole e allargare il range di ip gestiti, in modo da comprendere sia quelli assegnati al load balancer sia quello virtuale dell'endpoint delle api di Kubernetes.

Una volta fatta tutta questa preparazione si può lanciare lo script ansible con

```bash
ansible-playbook site.yml -i inventory/my-cluster/hosts.ini --ask-become-pass
```

e inserire la password per i comandi che richiedono i permessi di amministratore.

Lo script frulla qualche minuto e nella console è possibile visualizzare lo stato di ciascuna operazione su ciascuno dei nodi indicati nel file di inventory.

Se qualcosa andasse storto si può annullare tutto con

```bash
ansible-playbook reset.yml -i inventory/my-cluster/hosts.ini --ask-become-pass
```

(io nel dubbio mi sono fatto dei backup delle vm su Proxmox)

### 3. finalmente Kubectl

A questo punto il cluster k3s è installato e funzionante!

Però bisogna pilotarlo per poter configurare e installare cose, quindi serve `kubectl` e seguendo quindi [la documentazione](https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/#install-using-native-package-management):

```bash
sudo apt-get update
sudo apt-get install -y apt-transport-https ca-certificates curl

curl -fsSL https://pkgs.k8s.io/core:/stable:/v1.30/deb/Release.key | sudo gpg --dearmor -o /etc/apt/keyrings/kubernetes-apt-keyring.gpg
sudo chmod 644 /etc/apt/keyrings/kubernetes-apt-keyring.gpg

echo 'deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] https://pkgs.k8s.io/core:/stable:/v1.30/deb/ /' | sudo tee /etc/apt/sources.list.d/kubernetes.list
sudo chmod 644 /etc/apt/sources.list.d/kubernetes.list

sudo apt-get update
sudo apt-get install -y kubectl
```

e già che ci siamo installiamo anche l'utilissimo autocomplete per `zsh`:

```bash
echo 'source <(kubectl completion zsh)' >>~/.zshrc
source .zshrc
```

copiamo il file di configurazioni da uno dei nodi

```bash
scp filippo@192.168.0.xxx:~/.kube/config ~/.kube/config 
```

e testiamo il cluster

```bash
kubectl get nodes
```

se tutto è andato bene, la risposta sarà la lista dei nodi, con lo stato, il ruolo, da quanto tempo sono su e che versione di Kubernetes stanno usando

```bash
➜  ~ kubectl get nodes
NAME      STATUS   ROLES                       AGE     VERSION
kube-01   Ready    control-plane,etcd,master   1h      v1.29.4+k3s1
kube-02   Ready    control-plane,etcd,master   1h      v1.29.4+k3s1
kube-03   Ready    control-plane,etcd,master   1h      v1.29.4+k3s1
```

## 4. The end?

E questo è stato soltanto il setup iniziale! C'è ancora parecchia infrastruttura da mettere in piedi e ancora un mare di cose da imparare!

Anche se alla fine ho utilizzato uno script pronto all'uso, mi sono comunque picchiato con parecchi concetti che mi erano nuovi.

Prossimi step: installare un gestore di pacchetti (Helm), un proxy (Traefik) e un gestore di certificati (cert-manager). Dopodichè installare Rancher per gestire il cluster da una comoda interfaccia web e ArgoCD per riuscire a implementare configurazioni in maniera dichiarativa con GitOps.
