#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools

def setup():
    pisitools.dosed("qmotion.pro", "lrelease", "lrelease-qt4") 
    shelltools.system("qmake-qt4")

def build():
    autotools.make()

def install():
    pisitools.dobin("qmotion")
    pisitools.insinto("/usr/share/pixmaps", "qmotion.svg")
    pisitools.insinto("/usr/qt/4/translations", "*.qm")

    pisitools.dodoc("gpl-3.0.txt")
