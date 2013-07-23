#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "ufoai-%s-source" % get.srcVERSION()
datadir = "/usr/share/ufoai"
exefiles = ["ufo", "ufo2map", "ufoded"]

def setup():
    autotools.configure("--enable-release \
                         --enable-dedicated \
                         --enable-client \
                         --enable-master \
                         --enable-ufo2map \
                         --disable-paranoid \
                         --disable-profiling \
                         --with-gettext \
                         --with-ipv6 \
                         --with-sdl \
                         --with-vid-glx \
                         --with-shaders \
                         --with-snd-sdl \
                         --with-snd-alsa \
                         --with-snd-arts \
                         --with-snd-oss \
                         --without-snd-jack \
                         --without-openal \
                         --disable-paranoid \
                         --disable-profiling")

def build():
    autotools.make()
    autotools.make("lang")

def install():
    pisitools.insinto(datadir, "base")

    for f in exefiles:
        pisitools.dobin(f)

    pisitools.dodoc("BUGS", "CONTRIBUTORS", "COPYING", "README*")
