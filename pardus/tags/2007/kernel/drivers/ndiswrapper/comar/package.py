#/usr/bin/python

import os

def postInstall():
    os.system("/usr/bin/chmod 0755 /sbin/loadndisdriver")
    os.system("/usr/bin/chmod 0755 /usr/sbin/ndiswrapper")
