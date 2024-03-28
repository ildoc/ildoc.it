---
title: Nuovo blog?
date: 2015-03-25 11:06:50
tags: blog django
---

Cos'è cambiato? Nulla, *sembrerebbe*...
E invece sono passato da pelican a django, mantenendo quasi lo stesso layout.

Il vantaggio pratico è che posso scrivere i post direttamente dal web, ma la parte divertente è che il motore del blog [me lo scrivo da solo](https://github.com/ildoc/ildoc.it/).

Riprendendo in mano django dopo il primo faticosissimo approccio dell'anno scorso, mi sono reso conto che in realtà è molto più facile da usare di quanto ricordassi, probabilmente anche per le conoscenze acquisite in quest'ultimo anno.

I post su pelican erano scritti in markdown, per cui mi sono anche divertito a scrivere un [parser](https://github.com/ildoc/ildoc.it/blob/master/tools/migrate.py) che bene o male ha funzionato sui post pubblicati, in modo da non perdere niente.

Mi sto portando dietro roba del 2007 che, per quanto agghiacciante, sarebbe un peccato perdere...

I post continuerò a scriverli in markdown, grazie alle magie di python-markdown e django-pagedown, che mi permettono anche di avere un feedback real-time su come uscirà il post.
La sitemap dovrebbe funzionare, così come l'integrazione con twitter tramite IFTTT.

Quello che mi manca è un'interfaccia di scrittura post un po' più comoda del django-admin e un modo per uploadare le immagini da embeddare nei post.

Ci sono ancora dei link rotti nei post migrati, ma col tempo sistemerò tutto...
