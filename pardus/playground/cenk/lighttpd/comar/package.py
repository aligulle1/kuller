#!/usr/bin/python

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("/bin/chown lighttpd:lighttpd /var/run/lighttpd")
    os.system("/bin/chmod 0755 /var/run/lighttpd")

    os.system("/bin/chown lighttpd:lighttpd /var/log/lighttpd")
    os.system("/bin/chmod 0750 /var/log/lighttpd")

    os.system("/bin/chown lighttpd:lighttpd /var/lib/lighttpd")
    os.system("/bin/chmod 0750 /var/lib/lighttpd")

    os.system("/bin/chown lighttpd:lighttpd /var/cache/lighttpd -R")
    os.system("/bin/chmod 0750 /var/cache/lighttpd -R")
