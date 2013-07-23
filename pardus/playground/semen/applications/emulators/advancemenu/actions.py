#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    autotools.configure("--enable-expat \
                         --enable-zlib \
                         --enable-alsa \
                         --enable-fb \
                         --enable-slang \
                         --enable-ncurses \
                         --enable-freetype \
                         --enable-sdl \
                         --enable-asm")
def build():
    shelltools.export("STRIPPROG", "true")
    autotools.make()

def install():
    pisitools.dobin("advmenu")

    pisitools.dodoc("HISTORY", "README", "RELEASE", "doc/*.txt")
    pisitools.doman("doc/advmenu.1")
    pisitools.dohtml("doc/*.html")

