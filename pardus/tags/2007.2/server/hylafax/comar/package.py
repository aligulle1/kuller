#/usr/bin/python

import os

def postInstall():
    os.system("/usr/bin/chown -f -R dialout:dialout /var/spool/fax")
    os.system("/usr/bin/mkfifo -m 600 /var/spool/fax/FIFO")
    os.system("/usb/bin/chown dialout:dialout /var/spool/fax/FIFO")
