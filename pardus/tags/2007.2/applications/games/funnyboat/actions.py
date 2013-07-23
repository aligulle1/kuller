#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "funnyboat"
NoStrip = "/"

datadir = "/usr/share/funnyboat"

def install():
    pisitools.dodir(datadir)

    shelltools.copytree("data", "%s/%s/" % (get.installDIR(), datadir))
    shelltools.copy("*.py",  "%s/%s/" % (get.installDIR(), datadir))

    pisitools.dodoc("*.txt")
    pisitools.insinto("/usr/share/pixmaps", "data/kuvake.png", "funnyboat.png")

