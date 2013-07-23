#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get 

WorkDir = "Chromium-0.9"

def setup():
    # It's all about shell magic baby
    shelltools.export("CFLAGS", '%s -DPKGBINDIR=\\\"/usr/bin\\\" -DPKGDATADIR=\\\"/usr/share/chromium\\\"' % get.CFLAGS())

    pisitools.dosed("src/Makefile", "-O2 -DOLD_OPENAL", get.CFLAGS())
    pisitools.dosed("src-setup/Makefile", "-g", get.CFLAGS())
    pisitools.dosed("support/glpng/src/Makefile", "-O2", get.CFLAGS())
    
    autotools.rawConfigure("--enable-sdl --disable-smpeg --disable-setup --enable-vorbis")
    
def build():
    autotools.make()

def install():
    pisitools.dobin("bin/chromium")
    pisitools.dodoc("AUTHORS", "CHANGES", "LICENSE", "README*")
