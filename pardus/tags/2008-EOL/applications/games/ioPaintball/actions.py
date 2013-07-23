#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

builddir = "build/release-linux-i386"
datadir = "/usr/share/ioPaintball"

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
    pisitools.insinto("/usr/bin", "%s/ioq3ded.i386" % builddir, "ioPaintball-server")
    pisitools.insinto("/usr/bin", "%s/ioquake3.i386" % builddir, "ioPaintball")
    pisitools.insinto("/usr/bin", "%s/ioquake3-smp.i386" % builddir, "ioPaintball-smp")

    for so in ["baseq3", "missionpack"]:
        pisitools.doexe("%s/%s/*.so" % (builddir, so), "%s/%s/" % (datadir, so))

    pisitools.dodoc("BUGS", "ChangeLog", "NOTTODO", "TODO", "README", "*.txt")
