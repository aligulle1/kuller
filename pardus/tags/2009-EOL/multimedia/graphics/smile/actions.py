#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "smile"

def setup():
    shelltools.system("qmake-qt4 smile.pro")
    shelltools.system("lrelease-qt4 smile_tr.ts")

def build():
    autotools.make()

def install():
    pisitools.dobin("smile")

    for data in ["BIB_ManSlide", "Interface"]:
        pisitools.insinto("/usr/share/smile", data)

    pisitools.insinto("/usr/share/smile/translations/", "*.qm")

    pisitools.dodoc("copying")
