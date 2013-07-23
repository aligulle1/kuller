#!/usr/bin/python

import os

def postInstall():
    os.system("/usr/bin/chown root:wheel /usr/sbin/traceroute")
    os.system("/usr/bin/chmod 04710 /usr/sbin/traceroute")
