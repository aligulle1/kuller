#!/usr/bin/python

import os

def postInstall():
    # Autoload nvidia module
    if not open("/etc/modules.autoload.d/kernel-2.6").read().find("nvidia"):
        os.system("echo nvidia >> /etc/modules.autoload.d/kernel-2.6")
