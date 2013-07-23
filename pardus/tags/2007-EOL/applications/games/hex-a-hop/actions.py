#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

import os

WorkDir = "hex-a-hop"

cfg = {"CXX": get.CXX(),
       "CXXFLAGS": get.CXXFLAGS(),
       "NAME": "hex-a-hop",
       "DATADIR": "/usr/share/hex-a-hop"
       }

def fixperms(d):
    for root, dirs, files in os.walk(d):
        for name in dirs:
            shelltools.chmod(os.path.join(root, name), 0755)
        for name in files:
            shelltools.chmod(os.path.join(root, name), 0644)

def setup():
    fixperms("./")

def build():
    autotools.make('GCC=%(CXX)s \
                    CXXFLAGS="%(CXXFLAGS)s" \
                    NAME=%(NAME)s' % cfg)

def install():
    pisitools.dobin(cfg["NAME"])
    pisitools.dodir(cfg["DATADIR"])

    for d in ["graphics", "levels.dat"]:
        pisitools.insinto(cfg["DATADIR"], d)
