#!/usr/bin/python

import os

def postInstall():
    os.system("/usr/bin/chown dhcp:dhcp /var/run/dhcp -R")
    os.system("/usr/bin/chown dhcp:dhcp /var/lib/dhcp -R")
    os.system("/usr/bin/chmod 0755 /var/run/dhcp")
    os.system("/usr/bin/chmod 0755 /var/lib/dhcp")
