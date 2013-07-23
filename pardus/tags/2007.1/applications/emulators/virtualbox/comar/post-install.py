#!/usr/bin/python

import os

def postInstall():
    # Autoload vboxdrv module
    if not open("/etc/modules.autoload.d/kernel-2.6").read().find("vboxdrv"):
        os.system("echo vboxdrv >> /etc/modules.autoload.d/kernel-2.6")

    os.system("/sbin/modprobe vboxdrv")
