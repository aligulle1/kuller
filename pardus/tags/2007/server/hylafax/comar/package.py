#/usr/bin/python

import os

def postInstall():
    os.system("mkfifo -m 600 /var/spool/fax/FIFO")
    os.system("chown dialout:dialout /var/spool/fax/FIFO")
