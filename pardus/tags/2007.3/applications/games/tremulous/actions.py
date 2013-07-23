#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import get

import os

WorkDir = "tremulous-%s-src" % get.srcVERSION()
builddir = "build/release-linux-x86"
datadir = "/usr/share/tremulous"

def setup():
    pisitools.dosed("base/server.cfg", "set sv_hostname.*", 'set sv_hostname "Tremulous Server on Pardus"')

def build():
    autotools.make("BUILD_CLIENT=1 \
                    BUILD_SERVER=1 \
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
    shelltools.move("%s/tremded.x86" % builddir, "%s/tremulous-server" % builddir)

    for f in ["tremulous", "tremulous-server"]:
        shelltools.chmod("%s/%s" % (builddir, f), 0755)
        pisitools.dobin("%s/%s" % (builddir, f))

    for f in shelltools.ls("%s/base/" % builddir):
        if f.endswith(".so") and shelltools.isFile("%s/base/%s" % (builddir, f)):
            shelltools.chmod("%s/base/%s" % (builddir, f), 0755)
            pisitools.dobin("%s/base/%s" % (builddir, f), "%s/base/" % datadir)


