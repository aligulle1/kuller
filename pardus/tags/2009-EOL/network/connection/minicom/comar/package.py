#!/usr/bin/python

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("/bin/chown root:dialout /usr/bin/minicom")
    os.system("/bin/chmod 04755 /usr/bin/minicom")
