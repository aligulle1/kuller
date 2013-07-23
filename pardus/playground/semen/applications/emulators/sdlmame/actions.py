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

WorkDir = get.srcNAME() + get.srcVERSION().replace(".", "")

def build():
    #Use expat and zlib from system
    pisitools.dosed("makefile", "^BUILD_EXPAT", "# BUILD_EXPAT")
    pisitools.dosed("makefile", "^BUILD_ZLIB", "# BUILD_ZLIB")

    #shelltools.export("CFLAGS", "-Wno-unused -fomit-frame-pointer -fstrict-aliasing -fstrength-reduce -falign-functions=2 -falign-jumps=2 -falign-loops=2")

    #Use --as-needed
    pisitools.dosed("makefile", "^LDFLAGS = -Wl,--warn-common$", "LDFLAGS += -Wl,--warn-common -Wl,--as-needed")

    autotools.make("VERBOSE=1 SYMBOLS=1")


def install():
    for e in ("mame", "chdman", "ldverify", "jedutil", "romcmp", "testkeys"):
        pisitools.dobin(e)

    pisitools.insinto("/usr/share/sdlmame", "ui.bdf")
    pisitools.dodoc( "docs/*.txt", "SDLMAME.txt", "whatsnew.txt")

