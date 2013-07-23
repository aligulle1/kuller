#!/usr/bin/python

import os

def postInstall():
    os.system("/usr/bin/chown named:named /var/bind -R")
    os.system("/usr/bin/chown named:named /var/run/named -R")

    if not os.path.exists("/etc/bind/rndc.key"):
        os.system("/usr/sbin/rndc-confgen -r /dev/urandom -a -u named")
