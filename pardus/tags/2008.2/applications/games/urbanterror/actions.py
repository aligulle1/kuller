#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

client_builddir = "client/build/release-linux-i386"
server_builddir = "server/build/release-linux-i386"
datadir = "/usr/share/urbanterror"

def build():
    shelltools.cd("client")
    autotools.make('-j1 \
                    OPTIMIZE="%s" \
                    DEFAULT_BASEDIR="%s" \
                    BUILD_SERVER=0 \
                    BUILD_CLIENT=1 \
                    BUILD_CLIENT_SMP=1 \
                    BUILD_GAME_SO=1 \
                    BUILD_GAME_QVM=0 \
                    USE_SDL=1 \
                    USE_OPENAL=1 \
                    USE_CURL=1 \
                    USE_CODEC_VORBIS=1 \
                    USE_LOCAL_HEADERS=1' % (get.CFLAGS(), datadir))

    shelltools.cd("../server")
    autotools.make('-j1 \
                    OPTIMIZE="%s" \
                    DEFAULT_BASEDIR="%s" \
                    BUILD_SERVER=1 \
                    BUILD_CLIENT=0 \
                    BUILD_CLIENT_SMP=0 \
                    BUILD_GAME_SO=0 \
                    BUILD_GAME_QVM=0 \
                    USE_LOCAL_HEADERS=1' % (get.CFLAGS(), datadir))

def install():
    pisitools.dobin("%s/ioUrbanTerror.i386" % client_builddir)
    pisitools.dobin("%s/ioUrbanTerror-smp.i386" % client_builddir)
    pisitools.dobin("%s/ioUrTded.i386" % server_builddir)

    pisitools.rename("/usr/bin/ioUrbanTerror.i386", "urbanterror")
    pisitools.rename("/usr/bin/ioUrbanTerror-smp.i386", "urbanterror-smp")
    pisitools.rename("/usr/bin/ioUrTded.i386", "urbanterror-server")

    pisitools.doexe("%s/baseq3/*.so" % client_builddir, "%s/baseq3" % datadir)
    pisitools.doexe("%s/missionpack/*.so" % client_builddir, "%s/missionpack" % datadir)

    pisitools.dodoc("README.txt", "client/BUGS", "client/ChangeLog", "client/NOTTODO", "TODO", "README", "*.txt", "client/code/unix/LinuxSupport/*.txt")
