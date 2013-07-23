#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "mlt-%s" % get.srcVERSION()

def setup():
    pisitools.dosed("src/modules/sox/filter_sox.c", "#include <st.h>", "#include <sox/st.h>")

    autotools.configure("--enable-gpl \
                         --enable-shared \
                         --enable-theora \
                         --enable-vorbis \
                         --enable-libogg \
                         --enable-pp \
                         --enable-shared-pp \
                         --enable-motion-est \
                         --enable-avformat \
                         --enable-core \
                         --enable-dv \
                         --enable-feeds \
                         --enable-fezzik \
                         --enable-ffmpeg \
                         --enable-gtk2 \
                         --enable-inigo \
                         --enable-jackrack \
                         --enable-kino \
                         --enable-lumas \
                         --enable-motion_est \
                         --enable-normalize \
                         --enable-plus \
                         --enable-qimage \
                         --enable-resample \
                         --enable-sdl \
                         --enable-sox \
                         --enable-valerie \
                         --enable-vmfx \
                         --enable-vorbis \
                         --enable-westley \
                         --enable-xine \
                         --qimage-libdir=%s \
                         --qimage-includedir=%s/include" % (get.qtDIR(), get.qtDIR()))

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())