#!/usr/bin/python

import os

def postInstall():
    os.system("/usr/bin/chmod u+s,go-r /usr/bin/gpg2")
    os.system("/usr/bin/chmod u+s,go-r /usr/bin/gpg-agent")
