Title: Script standalone con Django
Date: 2015-05-11 04:46:58
Modified: 2015-05-12 14:58:55
Tags: django, virtualenv
Slug: script-standalone-con-django
Author: Doc
Status: Published

Volendo creare un tool di manutenzione/per operazioni batch/ecc. che necessita di interagire con, ad esempio, i modelli di un'app del nostro progetto con Django, è necessario caricare tutto l'ambiente all'interno del quale Django viene eseguito.

Ciò può essere fatto lanciando la shell di Django dal manage.py del nostro progetto:

    :::batch
    (ildoc) C:\Projects\ildoc.it>python manage.py shell
    Python 2.7.9 (default, Dec 10 2014, 12:28:03) [MSC v.1500 64 bit (AMD64)] on win32
    Type "help", "copyright", "credits" or "license" for more information.
    (InteractiveConsole)
    >>>

e da li poi utilizzare la funzione execfile() per lanciare il file che ci interessa

    :::batch
    >>> execfile("tools/manutenzione.py")

però questa cosa è abbastanza complessa, specialmente se si punta ad automatizzare il processo con dei jobs o dei trigger.

Quindi serve un modo per poter lanciare **direttamente** il nostro script.

La soluzione consiste nell'inserire queste righe all'inizio del nostro tool:

    :::python
    import os, sys
    
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Serve a specificare che ambiente usare
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mioprogetto.settings")
    sys.path.append(BASE_DIR)

    # Serve per caricare il settings.py
    os.chdir(BASE_DIR)

    # Serve a poter importare i modelli
    from django.core.wsgi import get_wsgi_application
    application = get_wsgi_application()

A questo punto potremo procedere importando quello che ci serve, esattamente come se stessimo lavorando all'interno del progetto.

E potremo finalmente eseguire il nostro tool scrivendo semplicemente in console

    :::batch
    (ildoc) C:\Projects\ildoc.it\tools>python manutenzione.py

Semplificandoci notevolmente la vita nel caso volessimo schedularne l'esecuzione.
