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

WorkDir = "blockout"
datadir = "/usr/share/blockout2"

def setup():
    pisitools.dosed("ImageLib/src/Makefile", "^CC.*gcc", "CC  = %s" % get.CC())
    pisitools.dosed("ImageLib/src/Makefile", "^CXX.*g\+\+", "CXX = %s" % get.CXX())
    pisitools.dosed("ImageLib/src/Makefile", "^CFLAGS[ ]*= \-O2", "CFLAGS    = %s " % get.CFLAGS())
    pisitools.dosed("ImageLib/src/Makefile", "^CXXFLAGS[ ]*= \-O2", "CXXFLAGS  = %s " % get.CXXFLAGS())

    pisitools.dosed("BlockOut_GL/Makefile", "^CXX.*g\+\+", "CXX     = %s" % get.CXX())
    pisitools.dosed("BlockOut_GL/Makefile", "-g -D_DEBUG", get.CXXFLAGS())

def build():
    shelltools.cd("ImageLib/src")
    autotools.make("-j1")
    shelltools.cd("../../BlockOut_GL")
    autotools.make("-j1")

def install():
    pisitools.dodir(datadir)
    for d in ["images", "sounds"]:
        pisitools.insinto(datadir, d)

    pisitools.dobin("BlockOut_GL/blockout2")
    pisitools.dodoc("README*")
