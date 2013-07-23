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

WorkDir = "warsow_%s_sdk" % get.srcVERSION()
source = "source"

def build():
    shelltools.cd(source)
    autotools.make('BINDIR=release \
                    BUILD_CLIENT=YES \
                    BUILD_SERVER=YES \
                    BUILD_IRC=YES \
                    BUILD_SND_QF=YES \
                    BUILD_SND_OPENAL=YES \
                    DEBUG_BUILD=NO \
                    SERVER_EXE=warsow-server \
                    CLIENT_EXE=warsow \
                    BASE_ARCH=i386 \
                    CFLAGS_RELEASE="%s -fno-strict-aliasing -ffast-math -funroll-loops" \
                    CC="%s" \
                    all' % (get.CFLAGS(), get.CC()))



def install():
    shelltools.cd(source)

    pisitools.dobin("release/warsow")
    pisitools.dobin("release/warsow-server")

    pisitools.dodir("/usr/share/warsow")
    shelltools.copytree("release/basewsw", "%s/usr/share/warsow/" % get.installDIR())
    shelltools.copytree("release/libs", "%s/usr/share/warsow/" % get.installDIR())

