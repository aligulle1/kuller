#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "kdiff3-0.9.95"

def setup():
    shelltools.cd("src-QT4")
    shelltools.system("qmake-qt4 PREFIX=/usr kdiff3.pro")

def build():
    shelltools.cd("src-QT4")
    autotools.make()

def install():
    pisitools.dobin("src-QT4/kdiff3")
    pisitools.insinto("/usr/share/icons/hicolor/16x16/apps/", "src-QT4/hi16-app-kdiff3.png", "kdiff3.png")
    pisitools.insinto("/usr/share/icons/hicolor/32x32/apps/", "src-QT4/hi32-app-kdiff3.png", "kdiff3.png")
    pisitools.insinto("/usr/share/icons/locolor/16x16/apps/", "src-QT4/lo16-app-kdiff3.png", "kdiff3.png")
    pisitools.insinto("/usr/share/icons/locolor/32x32/apps/", "src-QT4/lo32-app-kdiff3.png", "kdiff3.png")
    pisitools.dodoc("AUTHORS","ChangeLog", "COPYING", "README", "TODO")
