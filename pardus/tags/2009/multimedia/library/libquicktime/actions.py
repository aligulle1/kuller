#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import libtools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

KeepSpecial = ["libtool"]

def setup():
    shelltools.export("AUTOPOINT", "/bin/true")
    autotools.autoreconf("-fi")
    libtools.libtoolize("--force --copy")
    autotools.configure("--enable-shared \
                         --enable-asm \
                         --enable-firewire \
                         --enable-gpl \
                         --enable-mmx \
                         --disable-gtk \
                         --with-alsa \
                         --with-faad2 \
                         --with-ffmpeg \
                         --with-lame \
                         --with-libdv \
                         --with-libjpeg \
                         --with-libpng \
                         --with-opengl \
                         --with-schroedinger \
                         --with-x \
                         --with-x264 \
                         --without-doxygen \
                         --without-cpuflags")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # FIXME: keep la files if they are needed
    pisitools.dodoc("README", "TODO", "ChangeLog")
