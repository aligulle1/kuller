#/usr/bin/python

import os
import re

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("/usr/bin/install -d -m0755 /var/log/cups")
    os.system("/usr/bin/install -d -m0755 /var/spool")
    os.system("/usr/bin/install -m0700 -o pnp -d /var/spool/cups")
    os.system("/usr/bin/install -m1700 -o pnp -d /var/spool/cups/tmp")
    os.system("/usr/bin/install -m0711 -o pnp -d /etc/cups/certs")
    os.system("/usr/bin/install -d -m0755 /etc/cups/{interfaces,ppd}")

    # Fix the behavioural change introduced in cups 1.3.10 which broke
    # printing support on GTK+ applications.
    if os.path.exists("/etc/cups/client.conf.newconfig"):
        new = re.sub('^ServerName localhost.*$', 'ServerName /var/run/cups/cups.sock', open('/etc/cups/client.conf', 'r').read())
        open("/etc/cups/client.conf", "w").write(new)
