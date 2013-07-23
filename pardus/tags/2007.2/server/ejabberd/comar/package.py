#!/usr/bin/python

import os

def postInstall():
    os.system("/bin/bash /etc/jabber/self-cert.sh")
