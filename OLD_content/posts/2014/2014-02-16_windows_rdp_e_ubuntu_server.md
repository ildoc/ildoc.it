Title: Windows rdp e Ubuntu Server
Date: 2014-02-16 17:04:00
Modified: 2015-03-26 14:01:29
Tags: server, ubuntu, windows
Slug: windows-rdp-e-ubuntu-server
Author: Doc
Status: Published

Mettiamo per assurdo che uno voglia connettersi in desktop remoto da
Windows a Ubuntu server.  

Perchè, ad esempio, non può utilizzare
[PuTTY](https://www.chiark.greenend.org.uk/~sgtatham/putty/download.html)
perchè la porta 22 è bloccata sulla rete del suo ufficio.  

Per esempio, eh?

Che fare?  
Tanto per cominciare sarebbe il caso di installare un'inferfaccia
grafica su Ubuntu, dal momento che la versione server non ne ha una
(com'è normale che sia).

Dal momento che il server potrebbe non essere un missile, la scelta
ricade quindi su un ambiente desktop il più leggero possibile:
[LXDE](https://lxde.org/)

La installiamo con il comando  

    :::bash
    sudo apt-get install lxde

Ok, ma adesso? Come si fa la magia?  
Con il pacchetto [xrdp](https://www.xrdp.org/). (eterna lode a chi l'ha
scritto) che installiamo con  

    :::bash
    sudo apt-get install xrdp

e, ta-daaaan!
