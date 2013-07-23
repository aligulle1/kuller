#/usr/bin/python

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("/usr/bin/update-mime-database /usr/share/mime/")

def preRemove():
    os.system("/usr/bin/update-mime-database /usr/share/mime/")
