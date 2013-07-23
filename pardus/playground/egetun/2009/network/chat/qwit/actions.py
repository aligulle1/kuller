#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir = "%s-alpha-src" % get.srcDIR()

def setup():
    shelltools.system("lrelease-qt4 qwit.pro")
    shelltools.system("qmake-qt4")

    # Change C/XXFLAGS
    pisitools.dosed("Makefile", "CFLAGS        = -pipe -O2", "CFLAGS        = %s" % get.CFLAGS())
    pisitools.dosed("Makefile", "CXXFLAGS      = -pipe -O2", "CXXFLAGS      = %s" % get.CXXFLAGS())

def build():
    autotools.make()

def install():
    pisitools.dobin("qwit")
    pisitools.insinto("/usr/share/pixmaps", "images/qwit.png")

    pisitools.dodoc("AUTHORS", "COPYING", "README")
