#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005,2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.export("CFLAGS","%s -fsigned-char" % get.CFLAGS())

    autotools.configure("--enable-ogg-vorbis \
                         --enable-mad \
                         --enable-lame \
                         --enable-gsm \
                         --enable-oss-dsp \
                         --enable-alsa-dsp \
                         --enable-fast-ulaw \
                         --enable-fast-alaw")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dobin("src/libst-config")

    pisitools.insinto("/usr/include/sox", "src/st.h")
    pisitools.insinto("/usr/include/sox", "src/ststdint.h")

    # Doesn't allow shared libs and we need this static lib for mlt
    pisitools.dolib_a("src/libst.a")

    pisitools.dodoc("Changelog", "README", "TODO", "*.txt")
