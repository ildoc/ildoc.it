import os
from os.path import isfile, join

BASE_DIR = './content'

files = [f for f in os.listdir(BASE_DIR) if isfile(join(BASE_DIR, f))]
yeardir = set([d[:4] for d in files])


for f in files:
    path = BASE_DIR + '/' + f[:4]
    if not os.path.exists(path):
        os.mkdir(path)
    oldname = BASE_DIR + '/' + f
    newname = BASE_DIR + '/' + f[:4] + '/' + f[:10] + f[10:].replace('-', '_')
    os.rename(oldname, newname)
