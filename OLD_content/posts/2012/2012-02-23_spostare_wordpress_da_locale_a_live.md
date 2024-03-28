Title: Spostare Wordpress da locale a live
Date: 2012-02-23 16:36:00
Modified: 2015-03-24 16:09:17
Tags: wordpress, easyphp
Slug: spostare-wordpress-da-locale-a-live
Author: Doc
Status: Published


Chi si diverte a “smanettare” sul web spesso usa un ambiente locale come
[Wamp](https://www.wampserver.com/en/) o
[EasyPHP](2012-02-25_easyphp_un_webserver_in_pochi_click.md "EasyPHP: un webserver in pochi click")
per fare prove ed esperimenti.  
Ma come fare se poi si vuole rendere pubblico il proprio lavoro?  
Spesso basta semplicemente spostare qualche file nella cartella www del
proprio webserver e il gioco è fatto, altre volte bisogna lottare con
dipendenze di file e database.

Oggi, dopo vari test, ero riuscito ad ottenere una combinazione di
plugin ottimale per il mio Wordpress e volevo mettere online quanto
fatto, senza rischiare di perdere nulla.

Ed ecco come ho fatto, in pochi e semplici passaggi:

1.  Ho disabilitato TUTTI i plugin dal Wordpress nell’ambiente di prova
2.  Ho esportato il database in un file .sql
3.  Ho editato il file andando a sostituire tutte le occorrenze di
    “https://127.0.0.1” con “https://miosito.it”
4.  Ho installato un Wordpress nuovo di zecca sul mio host
5.  Ho sostituito la cartella wp-content del nuovo Wordpress con quella
    dell’ambiente di prova
6.  Ho cancellato il nuovo database e l’ho sostituito con il file .sql
    che ho esportato ed editato prima

*Et voilà!*  
Il gioco è fatto!

Dopodichè non mi è rimasto altro da fare che entrare nel pannello di
controllo del mio nuovo Wordpress, riattivare tutti i plugin e andare a
impostare tutte le opzioni come meglio pensavo.

Semplice, no?
