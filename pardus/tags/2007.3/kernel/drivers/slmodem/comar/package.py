#!/usr/bin/python

import os

def postInstall():
    os.system("/usr/bin/chown -R root:dialout /var/lib/slmodem")
