#!/usr/bin/python

import os

def postInstall():
    os.system("/usr/bin/chown root:wheel /usr/bin/ntpdate")
    os.system("/usr/bin/chmod 04710 /usr/bin/ntpdate")
