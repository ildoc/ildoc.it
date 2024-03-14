Title: DCOM e Kepware
Date: 2013-09-24 10:08:00
Modified: 2015-03-24 16:09:16
Tags: dcom, kepware, matrikon, opc
Slug: dcom-e-kepware
Author: Doc

Per riuscire a browsare/leggere/scrivere le tag e i loro valori su un
server kepware è necessario:

* registrare la libreria gbda\_aut.dll di grey box per la versione di windows che si sta usando (32/64bit) [Download](http://gray-box.net/download_daawrapper.php?lang=en)
* installare un OPC client (es.[Matrikon](http://www.matrikonopc.com/downloads/types/software/index.aspx))
* impostare le dcom del proprio computer come segue:
  * start -> esegui -> dcomcnfg
  * component services -> computer -> click destro su my computer -> properties
  * nella scheda com security entrare in ciascuno dei 4 pulsanti (edit limits, edit default) aggiungere gli utenti
    * everyone
    * self
    * system
    * network
    * interactive
    * anonymous logon

    e settare a TUTTI allow a tutto
  * apply, ok, e riavviare

Non sarà esattamente il metodo corretto, però così funziona...
