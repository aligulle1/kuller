#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("/bin/chown -R cacti.apache /var/log/cacti")
    os.system("/bin/chown -R cacti.root /var/lib/cacti/rra")
