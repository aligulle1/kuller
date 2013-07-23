#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

shelltools.export("HOME", get.workDIR())

def setup():
    autotools.rawConfigure("--prefix=/usr \
                            --enable-verbose-build \
                            --backend=sdl \
                            --enable-alsa \
                            --enable-flac \
                            --enable-mad \
                            --enable-nasm \
                            --enable-vorbis \
                            --enable-zlib")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dohtml("doc/he/*.html")
    pisitools.dodoc("AUTHORS", "COPYING", "COPYRIGHT", "NEWS", "README", "TODO", "doc/he/*.txt")
