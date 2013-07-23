#!/usr/bin/python

import os

def postInstall():
    os.system("/bin/chown -R root:root /usr/nagios")
    os.system("/bin/chown -R nagios:nagios /etc/nagios")
    os.system("/bin/chown -R nagios:nagios /var/nagios")
    os.system("/bin/chown -R nagios:apache /var/nagios/rw")
    os.system("/bin/chmod ug+s /var/nagios/rw")
