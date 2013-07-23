#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="PokerTH-%s-2-src" % get.srcVERSION()

def setup():
    shelltools.system("qmake-qt4 pokerth.pro")

def build():
    autotools.make()

def install():
    pisitools.dobin("pokerth")
    pisitools.dobin("bin/*")

    shelltools.system("lrelease-qt4 ts/pokerth_tr.ts -qm data/translations/pokerth_tr.qm")

    pisitools.insinto("/usr/share/pokerth","data")
    pisitools.insinto("/usr/share/pixmaps","pokerth.png")
    pisitools.insinto("/usr/share/applications", "pokerth.desktop")

    pisitools.dodoc("ChangeLog", "COPYING", "TODO", "docs/net_protocol.txt")
