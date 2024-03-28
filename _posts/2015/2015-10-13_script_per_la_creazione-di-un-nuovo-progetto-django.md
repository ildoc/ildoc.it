---
title: Script per la creazione di un nuovo progetto Django
date: 2015-10-13 09:39:35
tags: django
---

Per semplificarmi un po' la vita mi sono fatto un piccolo scriptino per facilitarmi la creazione di un nuovo progetto Django, con annesso ambiente virtuale (e pure un .bat per quando sviluppo da [windows]({% post_url 2015/2015-03-02-django-e-virtualenv-su-windows %}))

```shell
#!/bin/bash
YEAR=$(date +"%Y")

echo "[+]Creazione env"
python3 -m venv /envs/$1
source /envs/$1/bin/activate
echo "[+]Aggiornamento pip"
pip install -q -U pip
echo "[+]Installazione Django"
pip install -q django
cd $HOME/Projects/
echo "[+]Creazione progetto"
django-admin startproject $1
cd $1

echo "[+]Creazione cartelle"
mkdir static
mkdir templates
mkdir templates/admin

echo "[+]Creazione .gitignore"
cat <<EOF > .gitignore
*.py[cod]
*.sqlite3

assets/
*/__pycache__

access.log
error.log
EOF

cat <<EOF > windows.bat
start c:\Envs\$1\Scripts\activate.bat
atom .
EOF

echo "[+]Creazione LICENSE"
cat <<EOF > LICENSE
The MIT License (MIT)

Copyright (c) $YEAR $1 (ildoc.it)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
EOF

echo "[+]Creazione requirements.txt"
pip freeze > requirements.txt
echo "[+]Init del repository"
git init
echo "[+]Commit iniziale"
git add --all
git commit -m "first commit"
echo "[+]Avvio di Atom"
atom .
```
