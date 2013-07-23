#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

# WorkDir = "warsow_%s_sdk" % get.srcVERSION()
WorkDir = "warsow_0.32"
source = "source"
arch = "i386"

def build():
    shelltools.cd(source)
    autotools.make('BINDIR=release \
                    BUILD_CLIENT=YES \
                    BUILD_SERVER=YES \
                    BUILD_IRC=YES \
                    BUILD_SND_QF=YES \
                    BUILD_SND_OPENAL=YES \
                    DEBUG_BUILD=NO \
                    BASE_ARCH=%s \
                    CFLAGS_RELEASE="%s -fno-strict-aliasing -ffast-math -funroll-loops -DNDEBUG" \
                    CC="%s" \
                    all' % (arch, get.CFLAGS(), get.CC()))

                    # shell scripts override these, disabling for now
                    # SERVER_EXE=warsow-server \
                    # CLIENT_EXE=warsow \

def install():
    pisitools.dodoc("../docs/*")
    shelltools.cd(source)

    pisitools.insinto("/usr/bin", "release/warsow.%s" % arch, "warsow")
    pisitools.insinto("/usr/bin", "release/wsw_server.%s" % arch, "warsow-server")

    pisitools.dodir("/usr/share/warsow")
    shelltools.copytree("release/basewsw", "%s/usr/share/warsow/" % get.installDIR())
    shelltools.copytree("release/libs", "%s/usr/share/warsow/" % get.installDIR())

