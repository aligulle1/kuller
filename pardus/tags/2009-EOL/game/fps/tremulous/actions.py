#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import get

import os

WorkDir = "tremulous-%s-src" % get.srcVERSION()
builddir = "build/release-linux-x86"
datadir = "/usr/share/tremulous"

def setup():
    pisitools.dosed("misc/server.cfg", "set sv_hostname.*", 'set sv_hostname "Tremulous Server on Pardus"')

def build():
    autotools.make("BUILD_CLIENT=1 \
                    BUILD_CLIENT_SMP=1 \
                    BUILD_SERVER=1 \
                    BUILD_GAME_SO=0 \
                    BUILD_GAME_QVM=0 \
                    CC=%s \
                    DEFAULT_BASEDIR=%s \
                    USE_CODEC_VORBIS=1 \
                    USE_OPENAL=1 \
                    USE_LOCAL_HEADERS=0 \
                    OPTIMIZE=" % (get.CC(), datadir))

def install():
    pisitools.insinto("/usr/share/pixmaps", "misc/tremulous.xpm")
    pisitools.dodir("%s/base" % datadir)

    shelltools.move("%s/tremulous.x86" % builddir, "%s/tremulous" % builddir)
    shelltools.move("%s/tremulous-smp.x86" % builddir, "%s/tremulous-smp" % builddir)
    shelltools.move("%s/tremded.x86" % builddir, "%s/tremulous-server" % builddir)

    for f in ["tremulous", "tremulous-smp", "tremulous-server"]:
        shelltools.chmod("%s/%s" % (builddir, f), 0755)
        pisitools.dobin("%s/%s" % (builddir, f))

    for f in shelltools.ls("%s/base/" % builddir):
        if f.endswith(".so") and shelltools.isFile("%s/base/%s" % (builddir, f)):
            shelltools.chmod("%s/base/%s" % (builddir, f), 0755)
            pisitools.dobin("%s/base/%s" % (builddir, f), "%s/base/" % datadir)


