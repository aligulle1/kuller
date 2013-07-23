#!/usr/bin/python

import os

def postInstall():
    os.system("/usr/bin/chmod 4777 /var/run/jack")
