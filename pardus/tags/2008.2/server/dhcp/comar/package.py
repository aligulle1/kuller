#!/usr/bin/python

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("/bin/chown dhcp:dhcp /var/run/dhcp -R")
    os.system("/bin/chown dhcp:dhcp /var/lib/dhcp -R")
    os.system("/bin/chmod 0755 /var/run/dhcp")
    os.system("/bin/chmod 0755 /var/lib/dhcp")
