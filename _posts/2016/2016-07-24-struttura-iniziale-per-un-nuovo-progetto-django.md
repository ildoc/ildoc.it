---
title: Struttura iniziale per un nuovo progetto Django
date: 2016-07-24 20:33:16
categories: tutorial
Tags: python, django, tutorial
---
Stiamo per iniziare un nuovo progetto con Django e la domanda che ci poniamo è: "C'è un modo per strutturare il progetto in maniera che sia modulare, facile da navigare e da manutenere?"

Si, e ora vi spiego quello che ho adottato io:

L'ambiente virtuale
----------------------
Innanzitutto è necessario contenere e rendere replicabile ovunque il nostro ambiente di sviluppo.

In python2 c'era un fantastico pacchetto di nome `virtualenvwrapper`, ma visto che ormai siamo nel 2016 utilizzeremo python3, quindi apriamo una shell e scriviamo (su Linux):

```bash
python3 -m venv /path/dove/vivrà/il/nostro/ambiente/nomeambiente
```

su Windows invece il comando è praticamente uguale:

```powershell
python -m venv C:\path\dove\vivrà\il\nostro\ambiente\nomeambiente
```

nel percorso che avete specificato verrà creata una folder che conterrà un'installazione pulita di python3 che andremo a usare per sviluppare il progetto.

Una volta creato l'ambiente andiamo ad attivarlo, su Linux con:
```bash
source /path/[...]/nomeambiente/bin/activate
```
e su Windows con:
```powershell
C:\path\[...]\nomeambiente\Scripts\activate.bat
```

a conferma dell'attivazione troveremo `(nomeambiente)` all'inizio della riga di comando della nostra shell.

A questo punto non ci resta che installare Django con:

```bash
pip install django
```

Creazione del progetto
----------------------
Fin qui ci siamo preparati il "tavolo da lavoro", ora non ci resta che cominciare a costruire.

Quindi per cominciare iniziamo col creare il nostro progetto:

```bash
django-admin startproject mioProgetto
```

Il comando appena lanciato produrrà lo scheletro di default di Django, in una struttura a mio avviso un po' criptica.

```
mioProgetto/
|-- manage.py
`-- postdjango
    |-- __init__.py
    |-- settings.py
    |-- urls.py
    `-- wsgi.py
```

Non ho mai trovato molto senso nel creare una folder col nome del progetto... ...all'interno della folder col nome del progetto!, poi, girovagando su Github, mi sono imbattuto nel sorgente del sito [djangopackages.com](https://djangopackages.com) ([qui](https://github.com/pydanny/djangopackages) il sorgente) sviluppato da pydanny, l'autore di [Two Scoops of Django](https://amzn.to/2aiPUq2), che a mio avviso è la BIBBIA di Django.

E ho scoperto che la metodologia usata da pydanny è estremamente funzionale, così ho deciso di adottarla.

Dunque: il nostro obbiettivo è far fuori la folder col nome del progetto in maniera da rendere il suo contenuto organizzato meglio.

Quindi cominciamo con lo spostare tutti i file nel livello superiore, e cancelliamo la cartella vuota:

```
postdjango/
|-- __init__.py
|-- manage.py
|-- settings.py
|-- urls.py
`-- wsgi.py
```

I settings facilmente possono crescere sia di dimensione, sia di numero di file, quindi creiamo una cartella `settings` apposta, rendiamola un modulo creando al suo interno un file `__init__.py` e spostiamoci dentro il nostro `settings.py`, rinominandolo `base.py`.

In quest'ultimo file possiamo tenere, ad esempio, tutte le impostazioni che saranno condivide dagli altri settings.

Giusto per dare un senso a questa suddivisione, possiamo creare un piccolo file `nginx.py` dove metteremo le configurazioni specifiche al deploy:

```python
from .base import *

ALLOWED_HOSTS = ['miosito.it']
```

La nostra struttura ora sarà così:

```
mioProgetto/
|-- settings
|   |-- base.py
|   |-- __init__.py
|   `-- nginx.py
|-- __init__.py
|-- manage.py
|-- urls.py
`-- wsgi.py
```

Più comprensibile, no?

Ora andiamo a sistemare i riferimenti saltati nei vari file:

```python
# ROOT_URLCONF = 'mioProgetto.urls'
ROOT_URLCONF = 'urls'

[...]

# WSGI_APPLICATION = 'mioProgetto.wsgi.application'
WSGI_APPLICATION = 'wsgi.application'
```
{: file="settings/base.py"}

```python
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mioProgetto.settings")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.base")
```
{: file="manage.py"}

```python
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mioProgetto.settings")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.base")
```
{: file="wsgi.py"}

Fine. Ora abbiamo una base più coprensibile e possiamo cominciare a costruire il nostro progetto.
