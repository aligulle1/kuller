#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import crosstools as autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    autotools.configure('--enable-fbdev \
                         --enable-jpeg \
                         --enable-png \
                         --enable-gif \
                         --enable-freetype=yes \
                         --enable-multi \
                         --enable-sysfs \
                         --disable-sdl \
                         --disable-multi \
                         --disable-static \
                         --enable-zlib \
                         --disable-x11 \
                         --enable-video4linux \
                         --enable-video4linux2 \
                         --with-inputdrivers="all" \
                         --with-gfxdrivers=none \
                         --disable-vnc \
                         --disable-libmpeg3')

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dohtml("docs/html/")
    pisitools.dodoc("AUTHORS", "ChangeLog", "NEWS", "README*", "TODO", "fb.modes")

