#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("/bin/chmod 0750 /etc/bugzilla")

    if not os.path.exists("/etc/bugzilla/localconfig"):
        os.chdir("/usr/share/bugzilla")
        os.system("./checksetup.pl")

    os.system("/bin/chown -R root:apache /etc/bugzilla")
