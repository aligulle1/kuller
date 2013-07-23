#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="."

def setup():
    shelltools.system("qmake-qt4")

def build():
    autotools.make()

def install():
    pisitools.dobin("screenie")

    pisitools.insinto("/usr/share/applications", "screenie.desktop")
    pisitools.insinto("/usr/share/pixmaps", "resources/screenie.png")

    shelltools.system("lrelease-qt4 screenie.pro")
    pisitools.insinto("/usr/share/screenie", "l10n/*.qm")

    pisitools.dodoc("LICENSE.GPL*")
