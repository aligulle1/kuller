#!/usr/bin/python

import os

def postInstall():
    os.system("/usr/bin/chmod 2755 /usr/sbin/mlock")
    os.system("/usr/bin/chown root:mail /usr/sbin/mlock")
