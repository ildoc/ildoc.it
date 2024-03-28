---
title: Richiedere i permessi di amministratore per l'esecuzione di un programma
date: 2013-09-26 19:22:00
tags: c# permessi visual-studio
---

Per eseguire alcune funzioni, come ad esempio lanciare o stoppare dei
servizi, è necessario disporre dei permessi di amministratore del
sistema.  
Inoltre, è una funzione che può tornare utile se si vuole limitare
l'accesso a determinati programmi in base ai permessi utente.

Solitamente si clicca con il tasto destro sul programma in questione e
si seleziona "Esegui come amministratore", o si entra nelle proprietà e
si imposta "esegui sempre come amministratore", ma bisogna ricordarsi di
farlo!

E se si vende il programma? E se si passa a un amico?  
C'è un modo più semplice per avere la certezza che il programma verrà
SEMPRE eseguito con i permessi corretti?

Ovviamente si! :D

In Visual Studio, bisogna aggiungere un file di manifesto alla nostra
soluzione:  
per farlo, click destro -> aggiungi -> nuovo elemento -> e
selezioniamo "File manifesto applicazione"

Al suo interno, assicuriamoci che ci sia questo:

```xml
<trustinfo xmlns="urn:schemas-microsoft-com:asm.v2">
  <security>  
    <requestedprivileges xmlns="urn:schemas-microsoft-com:asm.v3">  
      <requestedexecutionlevel level="requireAdministrator" uiaccess="false"></requestedexecutionlevel>  
    </requestedprivileges>  
  </security>  
</trustinfo>
```

Ricompiliamo e il gioco è fatto.
