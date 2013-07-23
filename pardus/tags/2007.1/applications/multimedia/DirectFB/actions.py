#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005, 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.export("CPPFLAGS", "%s -I/usr/include/libmpeg3" % get.CXXFLAGS())

    autotools.configure("--enable-fbdev \
                         --enable-mmx \
                         --enable-sse \
                         --enable-libmpeg3 \
                         --enable-jpeg \
                         --enable-png \
                         --enable-gif \
                         --enable-freetype \
                         --enable-sysfs \
                         --disable-sdl \
                         --disable-multi \
                         --disable-debug \
                         --disable-static \
                         --enable-zlib \
                         --enable-x11 \
                         --enable-video4linux \
                         --enable-video4linux2 \
                         --with-gfxdrivers=\"all\"")
                        
def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("AUTHORS", "ChangeLog", "NEWS", "README*", "TODO")
    pisitools.dohtml("docs/html/")
