#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "Frodo-4.1b"

def setup():
    shelltools.unlink("%s/%s/Src/configure" % (get.workDIR(), WorkDir))
    shelltools.cd("Src")
    autotools.autoconf()
    autotools.configure("--enable-kbd-lang-us")

def build():
    shelltools.cd("Src")
    autotools.make()

def install():
    for f in ["Frodo", "FrodoPC", "FrodoSC", "TkGui.tcl"]:
        pisitools.dobin(f)
    for rom in ["1541 ROM", "Basic ROM", "Char ROM", "Kernal ROM"]:
        pisitools.insinto("/usr/share/frodo/", rom)
    pisitools.dodir("/usr/share/frodo/64prgs")
    pisitools.insinto("/usr/share/frodo/64prgs/", "64prgs/*")
    pisitools.dohtml("Docs/*")
