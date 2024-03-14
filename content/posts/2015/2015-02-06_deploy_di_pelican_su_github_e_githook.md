Title: Deploy di Pelican su GitHub e githook
Date: 2015-02-06 15:07:00
Modified: 2015-03-24 16:09:17
Tags: git, githook, pelican
Slug: deploy-di-pelican-su-github-e-githook
Author: Doc
Status: Published

Sto ancora giocherellando con [Pelican](http://blog.getpelican.com/) e cercavo un modo per committare i nuovi post UNA volta sola, senza dover committare una seconda volta gli html generati.

Ci sono riuscito abbastanza facilmente, ecco come:

##Prerequisiti:

* [Python](https://www.python.org/downloads/) >= 2.7
* [Git](http://git-scm.com/)
* un account su [GitHub](https://github.com/)
* tanta pazienza

Cominciamo:

##Setup dell'ambiente
Apriamo una shell e scriviamo

    :::bash
    pip install virtualenvwrapper
    mkvirtualenv pelican
    pip install pelican markdown

e dovremmo avere un virtualenv con pelican pronto all'installazione.

*God bless virtualenvwrapper*

Ora creaimo la cartella dove installeremo pelican:

    :::bash
    mkdir pelican
    cd pelican
    pelican-quickstart

a sto punto partirà l'installazione vera e propria, rispondete a tutte le domande ed è fatta.

##Deploy su GitHub
Su GitHub creiamo due nuovi repository con nome ***username*.github.io** e ***username*.github.io-source**, (dove *username* è chiaramente il vostro username di github).

Quello "-source" potete chiamarlo come vi pare.

Ora linkiamo il "-source" alla folder nella quale abbiamo appena installato pelican e committiamo tutto

    :::bash
    git init
    echo "output" > .gitignore
    git remote add origin git@github.com:username/username.github.io-source.git

dopodichè creiamo un submodule nella cartella output con

    git submodule add -f git@github.com:username/username.github.io.git output

a questo punto entriamo nella folder .git\hooks e creiamo il "trigger" che rigenererà il sito ad ogni push e committerà i file statici sul repository html

creiamo quindi un nuovo file "pre-push"

    :::bash
    #!/bin/sh
    cd output
    git fetch --all
    find * -maxdepth 0 -name '.git' -prune -o -exec rm -rf '{}' ';'
    cd ..
    pelican content -s publishconf.py
    cd output
    git add --all .
    git commit -am "automatic commit"
    git push origin master

    exit 0


adesso, tornando nella root di pelican potremmo fare

    :::bash
    git add .
    git commit -am "hello pelican"
    git push origin master

e se tutto è ok, dovrebbe partire da sola la seconda commit/push sul repository statico!
