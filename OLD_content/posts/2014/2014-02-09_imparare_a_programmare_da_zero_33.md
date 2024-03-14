Title: Imparare a programmare da zero - 3/3
Date: 2014-02-09 21:09:00
Modified: 2015-03-26 14:14:47
Tags: imparare a programmare
Slug: imparare-a-programmare-da-zero-33
Author: Doc
Status: Published

Questa è la terza e ultima parte di un trio di post volto a spiegare le
basi-basi della programmazione.  
Se parlo di torte e non capite perchè, leggete le parti precedenti :)  

* [Imparare a programmare da zero
1/3]({filename}2014-02-09_imparare_a_programmare_da_zero_13.md)
* [Imparare a programmare da zero
2/3]({filename}2014-02-09_imparare_a_programmare_da_zero_23.md)

Primi passi - Strutture comuni
------------------------------

Come le diverse lingue dei diversi paesi, i linguaggi di programmazione
hanno regole e sintassi diverse, ma sono tutte accomunate dallo stesso
scopo: comunicare con una macchina.  
E tutti contengono delle strutture "base" comuni che vengono utilizzate
poi come mattoncini lego per creare algoritmi complessi.

Vediamo quali sono:

### if - else

La struttra if-else direi che è la più comune in assoluto.  
Si può ricondurre facilmente a "SE - ALTRIMENTI" e serve a verificare
una condizione.

    if (condizione)
        fai questo
    else
        fai quest'altro

come si può vedere, se la (condizione) è vera fa "questo", altrimenti fa
"quell'altro"

esempio con la famosa torta:

    SE (la torta è cotta)
        tirala fuori dal forno
    ALTRIMENTI
        girala dalla parte meno cotta

### Cicli

I cicli sono l'altra struttura comune a tutti i linguaggi, servono ad
eseguire ripetutamente un gruppo di istruzioni finchè non si verifica
una certa condizione.  
Possono essere di due tipi, i cicli "for" e i cicli "while".

I cicli for partono dal presupposto che all'inizio dell'esecuzione si
sappia già quante saranno le ripetizioni e si possono interpretare come
un "Per n volte fai questo".

Esempio: è il mio compleanno e sulla torta ci sono 24 candeline.  
Il ciclo for allora potrebbe essere

    for 24 volte
        spegni una candelina

I cicli while invece basano il loro numero di esecuzioni sul verificarsi
o meno di una condizione e sono riconducibili a un "Finchè"

Il ciclo while della torta sarebbe:

    while ci sono ancora candeline accese
        spegni una candelina

La differenza dal ciclo for si ha perchè io eseguo l'azione di spegnere
una candelina tante volte finchè non ce ne sono più accese, a
prescindere dal numero.

Il ciclo while presenta anche una variante "do-while" che invece
verifica la condizione DOPO aver effettuato l'azione, del tipo:

    spegni una candelina
    fallo ancora finchè ci sono ancora candeline accese

In questo modo l'azione viene eseguita SEMPRE almeno una volta.

Questa situazione ad esempio produrrebbe un errore nel caso che
all'inizio del ciclo do-while non ci siano candeline accese.  
Una persona reale semplicemente non soffierebbe, ma i computer sono
macchine e non pensano e sicuramente alzerebbero tutto lo zucchero a
velo con una bella soffiata PRIMA di vedere se c'erano candeline accese
da spegnere.

La domanda che qui sorge spontanea quindi è: perchè usare i cicli
do-while che possono generare errori?  
Giusto, ma ci sono situazioni in cui tornano utili.

Sporcarsi le mani
-----------------

Bene, arrivati fin qui magari vi è venuta voglia di provare da soli,
eh?  
Quello che posso consigliare è aspettare ancora un attimo a buttarsi su
un linguaggio in particolare e soffermarsi ancora un momento sulle basi
logiche utilizzando il portale <http://code.org/learn>.

Code.org è un progetto molto interessante portato avanti con il
contributo dei "big" dell'informatica attuale con lo scopo di diffondere
una conoscenza che diventerà preziosissima nell'immediato futuro.

I tutorial sono guidati, suddivisi per argomento e ordinati per
difficoltà crescente e, anche se a prima vista possono apparire un po'
infantili forniscono basi importantissime (e sono anche divertenti da
fare).

Una volta conclusi quelli, potete cimentarvi con un linguaggio "vero", e
quello che consiglierei è partire con uno di alto livello, tipo Python,
nel quale ritroverete facilmente tutti i "comportamenti" che avete
osservato nei tutorial di Code.org.

Come link stavolta consiglio <http://learnpythonthehardway.org/> o
<http://www.codecademy.com/tracks/python>.  
Il metodo di studio proposto da quei siti funziona benone :)

Se durante l'approfondimento del mondo della programmazione voleste
mettere alla prova le conoscenze che avete acquisito, potete cimentarvi
nelle sfide di [Project Euler](http://projecteuler.net/problems) o
[CodeAbbey](http://codeabbey.com/).

Buon divertimento!
