#!/usr/bin/python

import os

def postInstall():
    if not os.path.exists("/etc/mail/aliases.db"):
        os.system("/usr/bin/newaliases")

    os.system("/usr/bin/chown root:postdrop /usr/sbin/postdrop")
    os.system("/usr/bin/chown root:postdrop /usr/sbin/postqueue")
    os.system("/usr/bin/chown root:mail /var/spool/mail")
    os.system("/usr/bin/chmod 02711 /usr/sbin/postdrop")
    os.system("/usr/bin/chmod 02711 /usr/sbin/postqueue")
    os.system("/usr/bin/chmod 0755 /var/spool/mail")
    os.system("/usr/bin/chmod 0600 /etc/postfix/saslpass")
