#!/usr/bin/python

import os

def postInstall():
    # Add festival user and group temporarily
    os.system("hav call User.Manager.addGroup gid 135 name festival")
    os.system("hav call User.Manager.addUser uid 135 name festival realname Festival shell /bin/false homedir /dev/null groups festival")

    os.system("/usr/bin/chown festival:festival /var/log/festival")
    os.system("/usr/bin/chown festival:festival /var/run/festival")
