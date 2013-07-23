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
    translations = ["cz", "de", "es", "ru", "tr"]
    for lang in translations:
        shelltools.system("lrelease-qt4 translations/qtemu_%s.ts" % lang)
        pisitools.insinto("/usr/share/qtemu/translations", "translations/qtemu_%s.qm" % lang)
    pisitools.insinto("/usr/share/qtemu", "qtemu")
    pisitools.insinto("/usr/share/qtemu", "help")

