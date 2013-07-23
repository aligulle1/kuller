#!/usr/bin/python

import os

def postInstall():
    os.system("/usr/bin/chown root:audio /opt/skype/skype")
    os.system("/usr/bin/chmod 0755 /opt/skype/skype")
