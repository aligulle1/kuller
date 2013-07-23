#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005, 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="Jubler-%s" % get.srcVERSION()

def setup():
    shelltools.system("ant jar")

def install():
    pisitools.insinto("/usr/share/java","dist/Jubler.jar","jubler.jar")
    pisitools.insinto("/usr/share/pixmaps/", "src/icons/frame.png", "jubler.png")
        
    pisitools.dodoc("LICENCE")
    pisitools.dodoc("README")
