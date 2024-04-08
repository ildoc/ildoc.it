Title: Installazione di ArchLinux
Date: 2017-10-26
Modified: 2017-10-26
Tags: tutorial, archlinux
Slug: installazione-di-archlinux
Author: Doc
Status: Draft

- scaricamento dell'iso
- creazione della virtual con virtualbox
- mount dell'iso
- boot arch linux x86_64

- loadkeys it
caricamento della tastiera italiana

- ping -c 3 google.com
check della connessione

----- recupero dei mirror più vicini da cui scaricare i pacchetti
- pacman -Syy
update di pacman

- pacman -S reflector
installazione di reflector

- reflector -c "IT" -f 12 -l 10 -n 12 --save /etc/pacman.d/mirrorlist
------

------ partizionare l'hard disk
- fdisk -l
lista dei dischi e delle partizioni

- cfdisk /dev/sda
avvio del tool di partizionamento

- [selezionare tipo dos ?]
- rimuovere la partizione esistenete, se c'è
- creare una nuova partizione
- impostarla come primary
- aggiungere il flag bootable
- write delle modifiche
- confermare con yes
- uscire con quit

- fdisk -l
controllare lista delle partizioni

- mkfs.ext4 /dev/sda1
format della partizione con formato ext4
------

- mount /dev/sda1 /mnt
mount della partizione

- lsblk
check dei mounting point

----- installazione OS
- pacstrap -i /mnt base base-devel
installazione dei pacchetti base (selezionare "all" per entrambe i gruppi)

- genfstab -U -p /mnt >> /mnt/etc/fstab
generazione fstab

- cat /mnt/etc/fstab
check del file fstab

- arch-chroot /mnt /bin/bash
login nel sistema appena installato

- nano /etc/locale.gen
- decommentare la lingua del sistema (en_US.UTF-8 UTF-8)
- chiudere e salvare

- locale-gen
generazione localizzazioni

- ls -sf /usr/share/zoneinfo/Europe/Rome /etc/localtime
set del fuso orario

- hwclock --systohc --utc
------

- echo arch > /etc/hostname
impostazione nome pc

- nano /etc/hosts
- replace degli <hostname> con il nome scelto prima

- systemctl enable dhcpcd
abilitazione servizi di rete

- passwd
impostazione password di root

- pacman -S grub
installazione di grub

- grub-install /dev/sda
installazione del bootloader

- grub-mkconfig -o /boot/grub/grub.cfg
creazione della configurazione di grub

- exit
logout dal sistema

- umount -R /mnt
unmount della partizione

- rimozione iso dalla virtual

- reboot

- login come root

- useradd -m -g users -G wheel -s /bin/bash <username>
aggiunta dell'utente

- passwd <username>
assegnazione della password per l'utente appena creato

- EDITOR=nano visudo
apertura del file dei sudoers

- decommentare la riga %wheel ALL=(ALL) ALL
- chiudere e salvare

- exit
logout

- login come <username>

- sudo pacman -S pluseaudio pluseaudio-alsa
installazione pacchetti per l'audio

- sudo pacman xorg -S xorg xorg-xinit
installazione X server

- scegliere 1 per usare la scheda grafica integrata (va bene per virtualbox)

- echo "exec gnome-session" > ~/.xinitrc

- sudo pacman -S gnome
installazione gnome

-sudo pacman -S gnome-extra

- startx
start della gui

