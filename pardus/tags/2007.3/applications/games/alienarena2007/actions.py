#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

datadir = "/usr/share/alienarena2007"

def setup():
    # Use system GL header
    pisitools.dosed("source/ref_gl/r_local.h", "glext.h", "GL/glext.h")
    pisitools.dosed("Makefile", "-ftree-vectorize")

def build():
    shelltools.export("CFLAGS", "%s -fno-strict-aliasing -Dstricmp=strcasecmp -D_stricmp=strcasecmp -I/usr/include/X11" % get.CFLAGS() + " `sdl-config --cflags`")

    autotools.make("SDLSOUND=1 \
                    OPTIM_LVL=2 \
                    LOCALBASE=/usr \
                    BUILD=ALL \
                    CC=%s \
                    OPTIMIZED_CFLAGS=yes" % get.CC())

def install():
    pisitools.dobin("release/crded")
    pisitools.dobin("release/crx")
    pisitools.dobin("release/crx.sdl")

    pisitools.rename("/usr/bin/crded", "alienarena2007-server")
    pisitools.rename("/usr/bin/crx", "alienarena2007-oss")
    pisitools.rename("/usr/bin/crx.sdl", "alienarena2007-sdl")

    pisitools.doexe("release/game.so", datadir)
    pisitools.dosym("%s/game.so" % datadir, "%s/arena/game.so" % datadir)
    pisitools.dosym("%s/game.so" % datadir, "%s/data1/game.so" % datadir)

    pisitools.insinto("%s/tools" % datadir, "Tools/LinuxScripts/*")

    pisitools.dodoc("docs/*")
