#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import get
from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

WorkDir="qeven_%s" % get.srcVERSION()

def setup():
    shelltools.system("qmake-qt4 PREFIX=/usr")

def build():
    autotools.make()

def install():
    pisitools.dobin("QEVEN")

    shelltools.system("lrelease-qt4 translation/*.ts")
    pisitools.insinto("/usr/share/qeven/locale/", "translation/*.qm")

    pisitools.insinto("/usr/share/icons/hicolor/32x32/apps", "Image/icon(32x32).png", "qeven.png")
    pisitools.insinto("/usr/share/icons/hicolor/64x64/apps", "Image/qeven(64x64).png", "qeven.png")

    pisitools.dodoc("AUTHORS", "CHANGELOG", "README", "TODO", "*.txt")
