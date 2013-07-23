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

WorkDir = "ufoai-2.0-RC6-source"
datadir = "/usr/share/ufoai"

libs = ["ref_glx.so", "ref_sdl.so", "snd_alsa.so", "snd_arts.so", "snd_oss.so", "snd_sdl.so"]
exes = ["ufo", "ufo2map", "ufoded"]

def setup():
    pisitools.dosed("Makefile", "^BASE_CFLAGS=", "BASE_CFLAGS=%s -I%s/include " % (get.CFLAGS(), get.kdeDIR()))

def build():
    autotools.make("BUILD_SDLUFO=YES \
                    BUILD_GLX=YES \
                    BUILD_DEDICATED=YES \
                    BUILD_ALSA=YES \
                    BUILD_OSS=YES \
                    BUILD_ARTS=YES \
                    BUILD_WITH_SHADER=YES \
                    HAVE_IPV6=NO \
                    HAVE_GETTEXT=NO \
                    BUILD_WITH_DGA=NO \
                    BUILD_WITH_VIDMODE=YES \
                    BUILD_WITH_MMX=YES \
                    BUILD_PARANOID=NO \
                    BUILD_FOR_PROFILING=NO \
                    BUILD_COMPILETOOLS=YES \
                    release")

def install():
    pisitools.dodir("%s/base" % datadir)
    shelltools.cd("releasei386")

    for f in libs:
        pisitools.dobin(f, datadir)

    for f in exes:
        pisitools.dobin(f, datadir)

    pisitools.dobin("game.so", "%s/base/" % datadir)
    pisitools.dodoc("../docs/*")

