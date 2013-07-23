#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

#WorkDir = "qtstumbler-%s" % get.srcVERSION()

def setup():
    shelltools.system("qmake-qt4 -unix -o Makefile qtstumbler.pro")

def build():
    autotools.make()

def install():
    pisitools.dobin("qtstumbler")

    pisitools.insinto("/usr/share/pixmaps/", "images/logo.png", "qtstumbler.png")

    pisitools.dodoc("docs/prezentace.odp", "docs/prezentace.pdf")
