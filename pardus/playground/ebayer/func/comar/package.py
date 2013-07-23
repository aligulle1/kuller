#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("touch /var/log/func/func.log")
    os.system("touch /var/log/func/audit.log")
    os.system("chmod 0600 /var/log/func/*")
