#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.system("qmake-qt4")

def build():
    autotools.make()

def install():
    pisitools.dobin("x2goclient")
    pisitools.insinto("/usr/share/pixmaps/x2goclient", "icons/*")
    pisitools.remove("/usr/share/pixmaps/x2goclient/x2go-*")
    pisitools.dodoc("AUTHORS", "LICENSE", "COPYING", "HOWTO.GPGCARD", "README")
