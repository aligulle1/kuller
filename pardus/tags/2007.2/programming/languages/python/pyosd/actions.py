#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pythonmodules 
from pisi.actionsapi import get

mods = "%s/%s/modules" % (get.docDIR(), get.srcTAG())

def setup():
    shelltools.chmod("modules/*", 0644)

def build():
    pythonmodules.compile()

def install():
    pythonmodules.install()

    pisitools.dodoc("AUTHORS", "COPYING", "README*", "NEWS")
    pisitools.dohtml("pyosd.html")
    pisitools.insinto(mods, "modules/*")

