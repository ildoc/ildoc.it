---
title: "gitScrape: ottenere un changelog dalle commit su GitHub"
date: 2013-09-17 11:27:00
tags: beautifulsoup github python
---

Attenzione: a prima vista potrebbe sembrare uno script perfettamente
inutile (e infatti lo è)

Un giorno ho sentito il bisogno di avere un changelog da mettere nel
progetto che stavo facendo, ma non avevo voglia di fare OGNI VOLTA
copia/incolla delle modifiche, datarle, suddividerle e cazzi vari.

Allora ho scritto questo, facendo uso di
[BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/ "BeautifulSoup").

```python
from bs4 import BeautifulSoup  
import urllib2

url = 'https://github.com/doc90/Organizr/commits/master' # url delle commit del branch

usock = urllib2.urlopen(url)  
data = usock.read()  
usock.close()

s=BeautifulSoup(data)  
for h3 in s.find_all('h3', {'class': 'commit-group-heading'}):  
    print h3.text  
    for li in h3.next_sibling.next_sibling.find_all('li', {'class':'commit commit-group-item js-navigation-item js-details-container'}):  
        print "- %s % s" % (li.find('a', {'class':'message'}).text, li.find('span', {'class':'sha'}).text)  
    print ''
```

Per ottenere una roba tipo:

```
Sep 10, 2013
- momentaneamente disattivati i recaptcha 26ed8c9216

Sep 09, 2013  
- fix minori 50763c8827  
- aggiunta bbcode 917a7c4505

Sep 08, 2013  
- aggiunte alcune immagini 0ae5963232  
- fix minori 188e74a37f  
- finito sistema patch f46744d22c  
- riscrittura blog 862537bf4e

Sep 07, 2013  
- inizio scrittura sistema patch 3d455d1bf3

Sep 02, 2013  
- fine passaggio a pdo 11d1134d30  
- inizio passaggio a pdo 4d03359967

Sep 01, 2013  
- cambiamenti minori f88259d247

Aug 30, 2013  
- inizio aggiunta date negli eventi 472cc4a402

Aug 29, 2013  
- rimosso globals.php, spostati funzioni e json, alcuni fix 7168c39aeb  
- aggiunto file di configurazione 166ed5b128  
- first commit cd1aeccd70
```
