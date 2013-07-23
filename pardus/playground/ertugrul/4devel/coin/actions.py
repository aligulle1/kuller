#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "Coin-%s" % get.srcVERSION()

def setup():
    autotools.configure("--enable-optimization \
                         --disable-3ds-import \
                         --enable-vrml97 \
                         --enable-man  \
                         --enable-system-expat \
                         --disable-html-help \
                         --enable-html \
                         --with-mesa \
                         --with-simage=/usr \
                         --with-freetype \
                         --with-bzip2 \
                         --with-fontconfig \
                         --with-openal \
                         --with-opengl \
                         --with-opengl-glu \
                         --with-x \
                         --with-zlib \
                         --enable-javascript-api \
                         --with-spidermokey \
                         --disable-java-wrapper")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "NEWS", "README*", "RELNOTES", "THANKS")

    # remove conflict man file with openssl
    pisitools.remove("/usr/share/man/man3/threads.3")
    # remove conflict man file with libftdi-devel
    pisitools.remove("/usr/share/man/man3/deprecated.3")
