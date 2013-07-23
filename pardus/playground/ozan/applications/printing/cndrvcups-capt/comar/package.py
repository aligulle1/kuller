#!/usr/bin/python

import os

def postInstall():
    if not os.path.exists("/var/ccpd"):
        os.mkdir("/var/ccpd")

        os.system("/usr/bin/mkfifo -m 600 /var/ccpd/fifo0")
        os.system("/usr/bin/chmod 777 /var/ccpd/fifo0")
        os.system("/usr/bin/chown root /var/ccpd/fifo0")

    if not os.path.exists("/var/captmon"):
        os.mkdir("/var/captmon")
        os.system("chown :pnpadmin /var/captmon")

    if not os.path.exists("/etc/cngplp/account"):
        os.makedirs("/etc/cngplp/account")
        os.chmod("/etc/cngplp/account", 0777)

    os.system("/sbin/ldconfig")

def preRemove():
    if os.path.exists("/var/ccpd"):
        for f in os.listdir("/var/ccpd"):
            os.unlink("/var/ccpd/%s" % f)
        os.rmdir("/var/ccpd")

    if os.path.exists("/var/captmon"):
        for f in os.listdir("/var/captmon"):
            os.unlink("/var/captmon/%s" % f)
        os.rmdir("/var/captmon")

    if os.path.exists("/etc/cngplp"):
        for f in os.listdir("/etc/cngplp/account"):
            os.unlink("/etc/cngplp/%s" % f)
        os.rmdir("/etc/cngplp/account")

