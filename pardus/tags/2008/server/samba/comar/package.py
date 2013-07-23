#/usr/bin/python

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    if not os.path.exists("/home/samba"):
        os.system("/bin/mkdir /home/samba")
        os.system("/bin/chmod 777 /home/samba")
