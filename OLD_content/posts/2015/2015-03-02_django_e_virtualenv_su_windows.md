Title: Django e virtualenv su Windows
Date: 2015-03-02 10:28:00
Modified: 2015-03-24 16:09:17
Tags: windows, django, virtualenv
Slug: django-e-virtualenv-su-windows
Author: Doc
Status:Published

Più che un post, questo è un appunto personale...
Per usare [django](https://www.djangoproject.com/) su windows dietro virtualenv occorre settare il path corretto per l'esecuzione dei file .py, altrimenti verrà utilizzato il "python.exe" di default

Questa operazione è fattibile con il comando (ovviamente da DENTRO il virtualenv)

    :::shell
    ftype Python.File="C:\Users\NOMEUTENTE\Envs\NOMEAMBIENTE\Scripts\python.exe" "%1" %*

Questa roba in teoria dovrebbe risulare automatica alla creazione del virtualenv, resta da capire se sia un baco di django o dell'ambiente...
