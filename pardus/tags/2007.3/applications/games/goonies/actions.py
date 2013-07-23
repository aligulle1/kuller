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

WorkDir = "goonies_r1-0-1"
datadir = "/usr/share/goonies"
datasources = ["graphics", "maps", "sound"]

def fixperms(d):
    for root, dirs, files in os.walk(d):
        for name in dirs:
            shelltools.chmod(os.path.join(root, name), 0755)
        for name in files:
            shelltools.chmod(os.path.join(root, name), 0644)

def setup():
    for d in datasources:
        fixperms(d)

    shelltools.copy("build/linux/Makefile", "src/")
    pisitools.dosed("src/Makefile", "^CC.*", "CC = %s" % get.CXX())
    pisitools.dosed("src/Makefile", "^CFLAGS.*", "CFLAGS = %s `sdl-config --cflags`" % get.CXXFLAGS())
    pisitools.dosed("src/Makefile", "^LDFLAGS.*", "LDFLAGS = %s `sdl-config --libs` -lSDL_image -lSDL_mixer -lSDL_sound -lGL -lGLU" % get.LDFLAGS())
    pisitools.dosed("src/Makefile", "^STRIP.*", "STRIP = echo")

def build():
    shelltools.cd("src")
    autotools.make("-j1")

def install():
    pisitools.dobin("src/goonies")
    pisitools.dodir(datadir)

    for d in datasources:
        pisitools.insinto(datadir, d)

    pisitools.dodoc("docs/*")

