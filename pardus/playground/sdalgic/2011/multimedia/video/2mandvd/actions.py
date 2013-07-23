#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import qt4

WorkDir="2ManDVD"

def setup():
    qt4.configure()

def build():
    qt4.make()

def install():
    shelltools.unlink("*.qm")
    shelltools.system("lrelease *.ts")
    pisitools.insinto("/usr/share/2ManDVD/", "Bibliotheque")
    pisitools.insinto("/usr/share/2ManDVD/", "*.qm")
    pisitools.insinto("/usr/share/2ManDVD/", "fake.pl")

    pisitools.insinto("/usr/share/2ManDVD/", "2ManDVD")
    pisitools.dosym("/usr/share/2ManDVD/2ManDVD", "/usr/bin/2ManDVD")

    pisitools.insinto("/usr/share/pixmaps", "Interface/mandvd.png", "2mandvd.png")

    pisitools.dodoc("README.txt")
