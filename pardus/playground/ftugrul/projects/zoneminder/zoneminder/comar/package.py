#!/usr/bin/python

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("/bin/chown -R mysql:mysql /var/lib/mysql/zm")
    os.system("/bin/chown apache:apache /var/run/zm")
    os.system("/bin/chown apache:apache /var/log/zoneminder")
    os.system("/bin/chmod 644 /etc/zm.conf")
