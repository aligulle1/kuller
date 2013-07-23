#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "mame-%s" % get.srcVERSION()

def build():
    #Use expat and zlib from system
    pisitools.dosed("makefile", "^BUILD_EXPAT", "# BUILD_EXPAT")
    pisitools.dosed("makefile", "^BUILD_ZLIB", "# BUILD_ZLIB")

    shelltools.export("CFLAGS", "-Wno-unused -fstrict-aliasing -fstrength-reduce -falign-functions=2 -falign-jumps=2 -falign-loops=2")

    #Use --as-needed
    pisitools.dosed("makefile", "^LDFLAGS = -Wl,--warn-common$", "LDFLAGS += -Wl,--warn-common -Wl,--as-needed")

    autotools.make("VERBOSE=1 SYMBOLS=1")


def install():
    if get.ARCH() == "x86_64":
        pisitools.dobin("mame64")
        pisitools.rename("/usr/bin/mame64", "mame")
    else:
        pisitools.dobin("mame")

    pisitools.insinto("/usr/share/mame", "sdlmame-ui.bdf", "ui.bdf")

    pisitools.dodoc( "docs/*.txt", "whatsnew.txt")
