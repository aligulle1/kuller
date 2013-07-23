#/usr/bin/python

import os

def postInstall():
    os.system("/usr/bin/install -d -m0755 /var/log/cups")
    os.system("/usr/bin/install -d -m0755 /var/spool")
    os.system("/usr/bin/install -m0700 -o pnp -d /var/spool/cups")
    os.system("/usr/bin/install -m1700 -o pnp -d /var/spool/cups/tmp")
    os.system("/usr/bin/install -m0711 -o pnp -d /etc/cups/certs")
    os.system("/usr/bin/install -d -m0755 /etc/cups/{interfaces,ppd}")
