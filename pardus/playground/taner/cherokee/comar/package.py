#!/usr/bin/python

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    if not os.path.exists("/var/log/cherokee"):
        os.system("/bin/mkdir -p /var/log/cherokee")
        os.system("/bin/chown apache:apache /var/log/cherokee")

    os.system("/bin/chmod 0755 /usr/share/cherokee/contrib/*")
    os.system("/bin/rm -f /usr/share/cherokee/contrib/*pyc")
