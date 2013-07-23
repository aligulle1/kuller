#!/usr/bin/python

import os

def postInstall():
    os.system("/usr/bin/chown ntp:ntp /var/lib/ntp -R")
