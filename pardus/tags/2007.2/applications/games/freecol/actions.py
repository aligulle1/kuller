#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir = 'freecol'

def setup():
    pisitools.remove("FreeCol.jar")
    pisitools.dosed('src/net/sf/freecol/FreeCol.java', 'saveDirectory, "freecol"', 'saveDirectory, ".freecol"')

def build():
    shelltools.system("ant")

def install():
    pisitools.insinto("/usr/share/pixmaps", "freecol.xpm")
    pisitools.insinto("/usr/share/freecol", "FreeCol.jar")
    pisitools.insinto("/usr/share/freecol/data", "data/*")
    pisitools.insinto("/usr/share/freecol/jars", "jars/*")

    pisitools.dodoc("README", "COPYING")
