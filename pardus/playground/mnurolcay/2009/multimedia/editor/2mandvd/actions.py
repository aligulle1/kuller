#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir="2ManDVD"

def setup():
    shelltools.system("qmake-qt4")

def build():
    autotools.make()

def install():
    pisitools.dobin("2ManDVD")

    shelltools.unlink("*.qm")
    shelltools.system("lrelease-qt4 *.ts")
    pisitools.insinto("/usr/share/2mandvd/locale", "*.qm")

    pisitools.insinto("/usr/share/pixmaps", "Interface/mandvd.png", "2mandvd.png")

    pisitools.dodoc("README.txt")
