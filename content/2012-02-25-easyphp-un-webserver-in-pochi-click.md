Title: EasyPHP: un webserver in pochi click
Date: 2012-02-25 09:42:00
Modified: 2015-03-24 16:09:17
Tags: risorse, easyphp, guida, guide
Slug: easyphp-un-webserver-in-pochi-click
Author: Doc

Primi passi con la programmazione web?  
Stiamo progettando un sito web?  
Vogliamo prendere confidenza con un software o un CMS per la nostra
community?

Ci serve quindi uno spazio dove “giocare”, e probabilmente non abbiamo
bisogno di complicarci la vita andando a registrare un dominio,
specialmente nel caso volessimo avere la possibilità di lavorare anche
offline.

Ecco che quindi ci viene incontro
[EasyPHP](http://easyphp.org/ "EasyPHP"), una piattaforma completa che
in qualche minuto ci permette di avere un ambiente di prova completo di
tutto.

Una volta
[scaricato](http://www.easyphp.org/download.php "Download EasyPHP") e
installato il pacchetto, avremo a disposizione il servizio dell’ultima
versione di Apache, l’interprete PHP, un database MySql accessibile
anche tramite PHPMyAdmin e tanto altro ancora, e non dovremo
preoccuparci di niente perchè è tutto già configurato!

A questo punto, accedendo a <http://127.0.0.1/home> oppure a
http://localhost/home dal nostro browser, avremo sottomano il pannello
di amministrazione di EasyPHP.

Come si potrà notare, nella Tray Bar sarà comparsa l’icona del
programma.  
Facendo un click destro sopra di essa e scegliendo “Esplora” si avrà
accesso alla cartella “www” dove si possono inserire i file che saranno
visibili all’indirizzo <http://127.0.0.1/> o http://localhost/.

Per quanto riguarda il database, l’installazione provvede a creare un
utente “root” senza password, ed è gestibile tramite l’interfaccia di
PHPMyAdmin o anche collegandosi con tool esterni come MySql Query
Browser specificando 127.0.0.1 come ip del server.

Ed eccoci pronti a sperimentare, proprio come se fossimo su un hosting
“vero”, con però la comodità di non dover passare per ftp o shell ssh.

Come si consiglia nel sito ufficiale però, questo è solo uno strumento
di testing e non è adatto a sopperire alle esigenze di chi cerca un
webserver vero e proprio per mettere online le proprie cose.  
Per quello è bene installare e configurare tutti i componenti uno per
uno e non accontentarsi di soluzioni già pronte per evitare di incappare
in spiacevoli inconvenienti, specialmente per quanto riguarda la
sicurezza dei dati.
