#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005, 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import libtools
from pisi.actionsapi import get

def setup():
    # seems mjpegtools does not play nicely with sse2 in gcc 3.x
    shelltools.export("CFLAGS", "%s -mno-sse2 -fno-strict-aliasing" % get.CFLAGS())
    shelltools.export("LDFLAGS", "%s -lpthread" % get.LDFLAGS())

    # all mighty strong m4 macros
    shelltools.export("AT_M4DIR", "m4")
    autotools.autoreconf()
    libtools.libtoolize("--force --copy")

    pisitools.dosed("configure", "ARCHFLAGS=.*", "ARCHFLAGS=")
    autotools.configure("--with-x \
                        --enable-cmov-extension \
                        --enable-largefile \
                        --enable-simd-accel \
                        --enable-xfree-ext \
                        --disable-static \
                        --with-dv-yv12 \
                        --with-quicktime \
                        --with-libpng \
                        --with-v4l \
                        --with-sdl \
                        --with-dv=/usr \
                        --with-libdv=/usr \
                        --with-jpeg-mmx=/usr/include/jpeg-mmx \
                        --without-gtk")


def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.dodoc("mjpeg_howto.txt", "README", \
                    "PLANS", "NEWS", "README.AltiVec", \
                    "README.avilib", "README.DV", "README.glav", \
                    "README.lavpipe", "README.transist", "TODO", \
                    "HINTS", "BUGS", "ChangeLog", "AUTHORS", "CHANGES")
