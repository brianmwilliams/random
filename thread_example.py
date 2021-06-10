#!/usr/bin/env python

from multiprocessing import Pool
import os
import subprocess

src = "{}/data/prod/".format(os.getenv("HOME"))
print(src)

def runprocess(folder):
    dest = "{}/data/prod_backup/".format(os.getenv("HOME"))
    print("rsyncing {} to {}".format(folder,dest))
    subprocess.call(["rsync", "-arq", folder, dest])

folders = []
for root, directory, files in os.walk(src):
    for filename in directory:
        folders.append(os.path.join(root, filename))

pool = Pool(len(folders))
pool.map(runprocess, folders)
