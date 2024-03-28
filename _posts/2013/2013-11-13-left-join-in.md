---
title: 'Left join "in"?'
date: 2013-11-13 17:18:00
tags: join, oracle, regex, sql
---

Mi sono trovato nella condizione di dover fare una join su più campi.  
Che stavano in una colonna sola.  
Separati da punti e virgola.

Prima di tentare il suicidio, ho googolato un pò e ho scoperto questo:

```sql
SELECT *  
FROM tabella1 LEFT JOIN tabella2 ON tabella2.colonnaA IN (  
    SELECT REGEXP_SUBSTR(tabella2.colonnaB,'[\^;]+', 1, level) FROM dual  
    CONNECT BY REGEXP_SUBSTR(tabella2.colonnaB, '[\^;]+', 1, level) IS NOT NULL  
);
```

Forse è una cosa risaputa, ma non la conoscevo...  
Sicuramente la riutilizzerò tantissimo.
