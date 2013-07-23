#!/usr/bin/python

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("/bin/chmod 0644 /etc/eciadsl/modems.db")
    os.system("/bin/chmod 0644 /etc/eciadsl/providers.db")
    os.system("/bin/chmod 0644 /etc/eciadsl/firmware00.bin")
    os.system("/bin/chmod 0644 /etc/eciadsl/synch01.bin")
    os.system("/bin/chmod 0644 /etc/eciadsl/modemeci.gif")
