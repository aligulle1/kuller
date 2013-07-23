#!/usr/bin/python

import os

def postInstall():
    os.system("/usr/bin/chown clamav:clamav /var/lib/clamav -R")
    os.system("/usr/bin/chown clamav:clamav /var/run/clamav -R")
    os.system("/usr/bin/chown clamav:clamav /var/log/clamav -R")
