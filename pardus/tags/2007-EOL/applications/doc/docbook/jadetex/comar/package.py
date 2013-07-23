import os

def postInstall():
    os.system("/usr/sbin/texmf-update")

def preRemove():
    os.system("/usr/sbin/texmf-update")
