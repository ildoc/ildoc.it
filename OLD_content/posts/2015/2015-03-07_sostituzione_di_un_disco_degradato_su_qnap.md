Title: Sostituzione di un disco degradato su QNAP
Date: 2015-03-07 10:26:00
Modified: 2015-04-28 12:26:45
Tags: nas, qnap
Slug: sostituzione-di-un-disco-degradato-su-qnap
Author: Doc
Status: Published

Dopo 2 anni di servizio, il disco 1 del mio QNAP TS-219P II (un  [WD Red 3TB](http://amzn.to/1wo7f8j)) ha deciso di lasciarmi.

Il QNAP è andato in modalità degraded, lucine rosse e beep ovunque...
Ho comprato un altro disco e poi mi sono messo a scartabellare l'internet per capire come sostituirlo senza perdere i dati.

Incredibile ma vero, la documentazione di QNAP è la più agghiacciante della storia.
Recentemente hanno rifatto il sito e non si sono minimamente preoccupati di mantenere i vecchi link, o almeno di reindirizzarli su pagine funzionanti -.-

Il forum poi, come sempre, non è d'aiuto per un cazzo ([questa discussione](http://forum.qnap.com/viewtopic.php?f=25&t=89512) ne è l'esempio)

Un [altro thread](http://www.hwupgrade.it/forum/showthread.php?p=40434840) su HWUpgrade mi ha fatto troppo tornare in mente questo

<center>![Wisdom of the Ancients](http://imgs.xkcd.com/comics/wisdom_of_the_ancients.png "All long help threads should have a sticky globally-editable post at the top saying 'DEAR PEOPLE FROM THE FUTURE: Here's what we've figured out so far ...")</center>

Comunque, alla fine ho scoperto che non è nemmeno necessario spegnere il qnap: la sostituzione può essere fatta al volo!

* si rimuove il disco danneggiato (ci saranno 2 beep da 1.5 secondi)
* si svitano le 4 viti che lo fissano a supporto e si sostituisce con uno nuovo
* si re-inserisce il nuovo disco (ci saranno di nuovo 2 beep da 1.5 secondi)

e in automatico il sistema comincerà con il ripristino del RAID

**GOD BLESS RAID 1**
