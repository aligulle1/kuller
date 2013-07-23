#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

WorkDir = "qtemu"

def build():
    shelltools.system("qmake-qt4")
    autotools.make()

def install():
    shelltools.system("lrelease-qt4 translations/qtemu_de.ts")
    shelltools.system("lrelease-qt4 translations/qtemu_tr.ts")
    pisitools.insinto("/usr/share/qtemu", "qtemu")
    pisitools.insinto("/usr/share/qtemu/translations", "translations/qtemu_de.qm")
    pisitools.insinto("/usr/share/qtemu/translations", "translations/qtemu_tr.qm")
    pisitools.insinto("/usr/share/qtemu", "help")

