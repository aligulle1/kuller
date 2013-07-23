#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "mjpegtools-1.9.0rc3"

def setup():
    shelltools.export("CFLAGS", "%s -fno-strict-aliasing" % get.CFLAGS())
    autotools.autoreconf("-fi -I m4")

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
                         --without-gtk")


def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("AUTHORS","ChangeLog","README*","mjpeg_howto.txt", "TODO")
