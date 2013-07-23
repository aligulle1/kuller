#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import get

WorkDir="comicmaster"

def setup():
    shelltools.system("qmake-qt4 ComicMaster.pro")

    pisitools.dosed("Makefile", "^CFLAGS .*", "CFLAGS = %s" % get.CFLAGS())
    pisitools.dosed("Makefile", "^CXXFLAGS .*", "CXXFLAGS = %s" % get.CXXFLAGS())
    pisitools.dosed("Makefile", "^LFLAGS .*", "LFLAGS = %s" % get.LDFLAGS())

def build():
    autotools.make()

def install():
    pisitools.dobin("ComicMaster")

    pisitools.insinto("/usr/share/pixmaps", "images/ComicMaster.png")

    pisitools.dodoc("CHANGES", "COPYING", "README")
