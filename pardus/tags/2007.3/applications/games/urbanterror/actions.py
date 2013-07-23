#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

import os

builddir = "build/release-linux-i386"
datadir = "/usr/share/urbanterror"

def build():
    autotools.make('OPTIMIZE="%s" \
                    DEFAULT_BASEDIR="%s" \
                    BUILD_SERVER=1 \
                    BUILD_CLIENT=1 \
                    BUILD_CLIENT_SMP=1 \
                    BUILD_GAME_SO=1 \
                    BUILD_GAME_QVM=1 \
                    USE_SDL=1 \
                    USE_OPENAL=1 \
                    USE_CODEC_VORBIS=1 \
                    USE_LOCAL_HEADERS=1' % (get.CFLAGS(), datadir))

def install():
    pisitools.dobin("%s/ioUrbanTerror.i386" % builddir)
    pisitools.dobin("%s/ioUrbanTerror-smp.i386" % builddir)
    pisitools.dobin("%s/ioUrTded.i386" % builddir)

    pisitools.rename("/usr/bin/ioUrbanTerror.i386", "urbanterror")
    pisitools.rename("/usr/bin/ioUrbanTerror-smp.i386", "urbanterror-smp")
    pisitools.rename("/usr/bin/ioUrTded.i386", "urbanterror-server")

    pisitools.doexe("%s/baseq3/*.so" % builddir, "%s/baseq3" % datadir)
    pisitools.insinto("%s/baseq3/vm/" % datadir, "%s/baseq3/vm/*" % builddir)

    pisitools.doexe("%s/missionpack/*.so" % builddir, "%s/missionpack" % datadir)
    pisitools.insinto("%s/missionpack/vm" % datadir, "%s/missionpack/vm/*" % builddir)

    pisitools.dohtml("code/unix/LinuxSupport/index.html")
    pisitools.dodoc("BUGS", "ChangeLog", "NOTTODO", "TODO", "README", "*.txt", "code/unix/LinuxSupport/CHANGES-1.32.txt")
