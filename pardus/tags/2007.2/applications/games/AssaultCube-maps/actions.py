#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

import os

NoStrip = "/"
datadir = "/usr/share/AssaultCube"

#sets = ["Filthy_RatTrap_v1.1/packages", \
#        "factory/bot", \
#        "factory/packages"]

# sets = ["Filthy_RatTrap_v1.1", \
#        "factory"]

hede = ["bot", "packages"]

def fixperms(d):
    for root, dirs, files in os.walk(d):
        for name in dirs:
            shelltools.chmod(os.path.join(root, name), 0755)
        for name in files:
            shelltools.chmod(os.path.join(root, name), 0644)

def setup():
    fixperms("./")

def install():
    #pisitools.dodir(datadir)

    #for s in sets:
    #    for d in shelltools.ls(s):
    #        if shelltools.isDirectory("%s/%s" % (s,d)):
    #            # shelltools.copytree("%s/%s" % (s, d), "%s/%s/" % (get.installDIR(), datadir))
    #            pisitools.insinto("%s/%s" % (datadir, d), "%s/%s/*" % (s, d))
    #            print "-- %s -- %s " % (s , d)

    #for d in ["bot/waypoints", "packages"]:
    #    pisitools.dodir("%s/%s" % (datadir, d))

    # pisi copytree cannot handle overlaying dirs, will make it by hand later on
    for d in hede:
        pisitools.insinto(datadir, d)

    for f in shelltools.ls("./"):
        if shelltools.isFile(f):
            if f.endswith(".cgz") or f.endswith(".cfg"):
                pisitools.insinto("%s/packages/maps/" % datadir, f)
            if f.endswith(".wpt"):
                pisitools.insinto("%s/bot/waypoints" % datadir, f)

