#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import libtools
from pisi.actionsapi import get

def setup():
    flags = "-O2 \
             -pipe \
             -mno-sse \
             -ffunction-sections"

    # shelltools.export("CFLAGS", "%s %s" % (get.CFLAGS(), flags))
    # shelltools.export("CXXFLAGS", "%s %s" % (get.CXXFLAGS(), flags))
    shelltools.export("CFLAGS", "%s -fno-strict-aliasing -fno-force-addr" % get.CFLAGS())
    shelltools.export("CXXFLAGS", "%s -fno-strict-aliasing -fno-force-addr" % get.CXXFLAGS())
    shelltools.export("CCASFLAGS","-Wa,--noexecstack")

    libtools.libtoolize("--force --copy")
    autotools.autoreconf("-fi")
    autotools.configure(" \
                      --prefix=/usr \
                      --mandir=/usr/share/man \
                      --disable-altivec \
                      --disable-artstest \
                      --disable-dxr3 \
                      --disable-gnome \
                      --disable-vidix \
                      --enable-aalib \
                      --enable-antialiasing \
                      --enable-asf \
                      --enable-directfb \
                      --enable-faad \
                      --enable-fb \
                      --enable-ffmpeg-popular-codecs \
                      --enable-ffmpeg-uncommon-codecs \
                      --enable-fpic \
                      --enable-ipv6 \
                      --enable-mmap \
                      --enable-mng \
                      --enable-modplug \
                      --enable-opengl \
                      --enable-samba \
                      --enable-xinerama \
                      --with-external-a52dec \
                      --with-external-ffmpeg \
                      --with-external-libmad \
                      --with-freetype \
                      --with-fontconfig \
                      --with-internal-vcdlibs \
                      --with-real-codecs-path=/usr/lib/essential \
                      --with-vorbis \
                      --with-wavpack \
                      --with-w32-path=/usr/lib/essential \
                      --with-x \
                      --with-xcb \
                      --with-xv-path=/usr/lib \
                      --without-esound \
                      --without-imagemagick \
                      --without-jack \
                      --disable-gdkpixbuf \
                      --disable-rpath \
                      --disable-syncfb \
                      --disable-optimizations \
                      --disable-dependency-tracking")

def build():
    autotools.make("-j1")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.removeDir("/usr/share/doc/xine")

    pisitools.dohtml("doc/faq/faq.html", "doc/hackersguide/*.html", "doc/hackersguide/*.png")
    pisitools.dodoc("AUTHORS", "ChangeLog", "README", "TODO", "doc/README*", "doc/faq/faq.txt")
