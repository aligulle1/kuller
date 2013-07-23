import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.chmod("/usr/bin/pinentry-qt4", 04755)
