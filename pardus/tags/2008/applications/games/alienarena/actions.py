#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

datadir = "/usr/share/alienarena"

def setup():
    # Use system GL header
    pisitools.dosed("ref_gl/r_local.h", "glext.h", "GL/glext.h")

def build():
    autotools.make("SDLSOUND=yes \
                    OPTIM_LVL=2 \
                    PREFIX=/usr \
                    LOCALBASE=/usr \
                    WITH_DATADIR=yes \
                    DATADIR=%s \
                    BUILD=ALL \
                    CC=%s \
                    OPTIMIZED_CFLAGS=yes" % (datadir, get.CC()))

def install():
    pisitools.dobin("release/crded")
    pisitools.dobin("release/crx")
    pisitools.dobin("release/crx.sdl")

    pisitools.rename("/usr/bin/crded", "alienarena-server")
    pisitools.rename("/usr/bin/crx", "alienarena-oss")
    pisitools.rename("/usr/bin/crx.sdl", "alienarena-sdl")

    pisitools.doexe("release/game.so", "%s/arena" % datadir)
    pisitools.dosym("%s/arena/game.so" % datadir, "%s/data1/game.so" % datadir)
