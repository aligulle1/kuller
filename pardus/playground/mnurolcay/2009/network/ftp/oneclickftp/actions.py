#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    shelltools.system("qmake-qt4")

    pisitools.dosed("Makefile", "^CXXFLAGS .*", "CXXFLAGS=%s" % get.CXXFLAGS())
    pisitools.dosed("Makefile", "^LFLAGS .*", "LFLAGS = %s" % get.LDFLAGS())

def build():
    autotools.make()

def install():
    autotools.rawInstall("INSTALL_ROOT=%s" % get.installDIR())

    pisitools.insinto("/usr/share/pixmaps", "res/icons/oneclickftp.png")

    pisitools.dodoc("CHANGELOG", "COPYING")
