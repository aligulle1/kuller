#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    f = open("/var/lib/misc/prelink.force", "w")
    f.close()
