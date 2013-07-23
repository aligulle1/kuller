#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    shelltools.unlinkDir("bin")
    shelltools.system("qmake-qt4")

def build():
    autotools.make()

def install():
    pisitools.dobin("rapid-down")

    pisitools.insinto("/usr/share/applications", "data/rapid-down.desktop")
    pisitools.insinto("/usr/share/pixmaps", "data/rapid-down.png")

    pisitools.dodoc("readme", "copying")
