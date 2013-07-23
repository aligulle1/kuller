#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    autotools.make('CC="%s" \
                    CFLAGS="%s" \
                    LDFLAGS="-L%s/pbm -L%s/pgm -L%s/pnm -L%s/ppm" \
                    LADD="-lm" \
                    JPEGINC_DIR=/usr/include \
                    PNGINC_DIR=/usr/include \
                    TIFFINC_DIR=/usr/include \
                    JPEGLIB_DIR=/usr/lib \
                    PNGLIB_DIR=/usr/lib \
                    TIFFLIB_DIR=/usr/lib \
                    LINUXSVGALIB="NONE" \
                    X11LIB=/usr/lib/libX11.so \
                    XML2LIBS="NONE" -j1' % (get.CC(),get.CFLAGS(),get.curDIR(),get.curDIR(),get.curDIR(),get.curDIR()))

def install():
    pisitools.dodir("/")
    autotools.make('LINUXSVGALIB="NONE" XML2LIBS="NONE" package pkgdir=%s/usr' % get.installDIR())

    for data in ["VERSION","pkginfo","README","config_template"]:
        pisitools.remove("/usr/%s" % data)

    for directory in ["misc","link","man/web"]:
        pisitools.removeDir("/usr/%s" % directory)

    pisitools.domove("/usr/man", "/usr/share")
    pisitools.dodoc("README", "doc/*LICENSE*")
