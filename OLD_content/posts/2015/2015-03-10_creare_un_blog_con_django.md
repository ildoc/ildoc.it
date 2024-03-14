Title: Creare un blog con Django
Date: 2015-03-10 09:58:00
Modified: 2015-05-07 08:17:25
Tags: blog, django, tutorial
Slug: creare-un-blog-con-django
Author: Doc
Status: Draft

Visto che mi sto pian piano costruendo [questo blog](https://github.com/ildoc/ildoc.it), cerco di farne un piccolo riassunto dello sviluppo.

Magari può venir bene a qualcuno come integrazione del [tutorial ufficiale](https://docs.djangoproject.com/en/dev/intro/tutorial01/)

#Installazione virtualenvwrapper e django
Per cominciare, se siamo su linux installiamo virtualenvwrapper (sempre sia lodato) con `pip install virtualenwrapper`, altrimenti scarichiamo e installiamo la [versione windows](https://pypi.python.org/pypi/virtualenvwrapper-win)

Fatto ciò, apriamo una shell e utilizziamo i seguenti comandi per creare un nuovo ambiente virtuale, installare l'ultima versione di Django e creare un file con la lista di pacchetti attualmente installati:

    :::bash
    $ mkvirtualenv djangoblog
    (djangoblog) $ pip install django
    (djangoblog) $ pip freeze > requirements.txt

Creare il file "requirements.txt", e mantenerlo aggiornato ogni volta che si installa un nuovo pacchetto, è importante, perchè permette di ricostruire un ambiente di sviluppo identico OVUNQUE, nel caso si voglia spostare il progetto per continuare gli sviluppi su un altro pc (o per deployarlo su un server, per esempio)

*Nota:* per entrare e uscire dal virtualenv, i comandi sono `workon [nome virtualenv]` e `deactivate`

#Startproject e startapp
Creiamo adesso lo scheletro della nostra applicazione


configurazione settings
definizione del modello
creazione viste
login e gestione permessi
