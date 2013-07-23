#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

datadir = "/usr/share/alienarena"
libdir = "/usr/lib/alienarena"

def setup():
    # Use system GL header
    pisitools.dosed("ref_gl/r_local.h", "glext.h", "GL/glext.h")

def build():
    autotools.make("CC=%s \
                    OPTIM_LVL=2 \
                    LOCALBASE=/usr \
                    SDLSOUND=yes \
                    WITH_DATADIR=yes \
                    WITH_LIBDIR=yes \
                    PREFIX=/usr \
                    DATADIR=%s \
                    LIBDIR=%s \
                    BUILD=ALL \
                    OPTIMIZED_CFLAGS=yes" % (get.CC(), datadir, libdir))

def install():
    pisitools.dobin("release/crded")
    pisitools.dobin("release/crx")
    # Probably removed
    # pisitools.dobin("release/crx.sdl")

    pisitools.rename("/usr/bin/crded", "alienarena-server")
    pisitools.rename("/usr/bin/crx", "alienarena")
    # Probably removed
    # pisitools.rename("/usr/bin/crx.sdl", "alienarena-sdl")

    pisitools.doexe("release/game.so", libdir)
    pisitools.doexe("release/arena/game.so", "%s/arena" % datadir)
