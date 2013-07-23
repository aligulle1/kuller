#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir = "lightfeather"

def setup():
    shelltools.system("./buildsys -l lightfeather.build")
    autotools.autoreconf("-fi")
    autotools.configure("--prefix=/usr \
                         --enable-static=no \
                         --enable-shared=yes \
                         --enable-doxygen \
                         --enable-internal-zlib=no \
                         --enable-internal-pnglib=no \
                         --enable-internal-jpeglib=no \
                         --enable-internal-freetype=no")

def build():
    autotools.make()

    # doc
    shelltools.system("doxygen doxygen.conf")

def install():
    autotools.install()

    # install headers correctly
    pisitools.removeDir("/usr/include")
    pisitools.insinto("/usr/include/", "include/lf/")

    pisitools.dohtml("doc/html/*.html", "doc/html/*.png")
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README.TXT", "RELEASE_NOTES")
