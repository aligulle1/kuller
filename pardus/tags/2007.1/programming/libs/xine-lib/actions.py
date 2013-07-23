#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import libtools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir= "xine-lib-%s" % get.srcVERSION().split('_')[1]

def setup():
    flags = "-mcpu=i686 \
             -O2 \
             -pipe \
             -frename-registers \
             -fomit-frame-pointer \
             -mno-sse \
             -ffunction-sections"

    shelltools.export("CFLAGS", "%s %s" % (get.CFLAGS(), flags))
    shelltools.export("CXXFLAGS", "%s %s" % (get.CXXFLAGS(), flags))
    shelltools.export("CCASFLAGS","-Wa,--noexecstack")

    shelltools.system("./configure \
                      --prefix=/usr \
                      --mandir=/usr/share/man \
                      --disable-gnome \
                      --disable-altivec \
                      --enable-ipv6 \
                      --enable-samba \
                      --enable-mng \
                      --enable-png \
                      --enable-faad \
                      --enable-flac \
                      --enable-speex \
                      --enable-modplug \
                      --with-ogg \
                      --with-vorbis \
                      --with-x \
                      --enable-xinerama \
                      --disable-vidix \
                      --disable-dxr3 \
                      --enable-directfb \
                      --enable-fb \
                      --enable-opengl \
                      --enable-aalib \
                      --enable-caca \
                      --enable-sdl \
                      --enable-libmad --with-external-libmad \
                      --enable-alsa \
                      --enable-arts \
                      --disable-esd \
                      --enable-ffmpeg \
                      --with-internal-vcdlibs \
                      --with-w32-path=/usr/lib/essential \
                      --with-xv-path=/usr/lib \
                      --with-external-ffmpeg \
                      --disable-optimizations \
                      --disable-jack \
                      --disable-dependency-tracking")

def build():
    autotools.make("-j1")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "README", "TODO", "doc/README*", "doc/faq/faq.txt")
    pisitools.dohtml("doc/faq/faq.html", "doc/hackersguide/*.html", "doc/hackersguide/*.png")

    pisitools.removeDir("/usr/share/doc/xine")

