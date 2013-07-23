import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("/usr/bin/motif-config -s")

def preRemove():
    os.system("/usr/bin/motif-config -s")
