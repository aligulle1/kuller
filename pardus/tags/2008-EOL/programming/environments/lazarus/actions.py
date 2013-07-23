#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006,2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

WorkDir = "lazarus"
NoStrip = [
        "/usr/share/lazarus/components",
        "/usr/share/lazarus/converter",
        "/usr/share/lazarus/debugger",
        "/usr/share/lazarus/designer",
        "/usr/share/lazarus/examples",
        "/usr/share/lazarus/ide",
        "/usr/share/lazarus/ideintf",
        "/usr/share/lazarus/lcl",
        "/usr/share/lazarus/languages",
        "/usr/share/lazarus/units"
        ]

def build():
    autotools.make("LCL_PLATFORM=gtk2 bigide tools -j1")

def install():
    pisitools.insinto("/usr/share", ".", "lazarus")

    pisitools.dosym("/usr/share/lazarus/lazarus", "/usr/bin/lazarus")
    pisitools.dosym("/usr/share/lazarus/images/ide_icon48x48.png", "/usr/share/pixmaps/lazarus.png")

    pisitools.dodoc("COPYING*", "README")
