#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def build():
    shelltools.export("CFLAGS", "-Wno-unused -fomit-frame-pointer -fstrict-aliasing -fstrength-reduce -falign-functions=2 -falign-jumps=2 -falign-loops=2")
    autotools.make("DISPLAY_METHOD=SDL")
    autotools.make("DISPLAY_METHOD=x11")

def install():
    pisitools.dosed("Makefile", "^PREFIX.*", "PREFIX=%s/usr" % get.installDIR())

    autotools.install("DISPLAY_METHOD=SDL")
    autotools.install("DISPLAY_METHOD=x11")

    pisitools.dobin("chdman")
    pisitools.dobin("xml2info")

    pisitools.insinto("/usr/share/xmame", "ctrlr")
    pisitools.dodoc("doc/changes.*", "doc/*.txt", ",mame/*" , "doc/xmamerc.dist", "README", "todo")
    pisitools.dohtml("doc/")

    # default to sdl since the client is a bit more featureful
    pisitools.dosym("xmame.SDL", "/usr/bin/xmame")
