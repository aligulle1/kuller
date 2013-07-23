#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir = 'ManDVD-2.4src'

def setup():
    shelltools.system("/usr/qt/3/bin/qmake mandvd.pro")

def build():
    autotools.make()

def install():
    pisitools.insinto("/usr/share/pixmaps", "mandvdico.png", "mandvd.png")
    pisitools.dobin("mandvd")
    pisitools.dodoc("COPYING")
