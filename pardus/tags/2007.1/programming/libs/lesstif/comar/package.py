import os

def postInstall():
    os.system("/usr/bin/motif-config -s")
    
def preRemove():
    os.system("/usr/bin/motif-config -s")
