#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    kdmpath = "/etc/X11/kdm/kdmrc4"
    rc =  open(kdmpath).read()
    kdmrc4 = open(kdmpath, "w")
    kdmrc4.write(rc.replace("kdm.pid", "kdm-kde4.pid"))
    kdmrc4.close()
