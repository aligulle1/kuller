#!/usr/bin/python

import os

def postInstall():
    os.system("/usr/bin/chown root:dialout /usr/bin/minicom")
    os.system("/usr/bin/chmod 04755 /usr/bin/minicom")
