#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "ffmpeg-%s" % get.srcVERSION().split('_')[-1]

def setup():
    # CPU thing is just used for CMOV detection
    autotools.rawConfigure("--cpu=i686 \
                            --prefix=/usr \
                            --mandir=/usr/share/man \
                            --enable-gpl \
                            --enable-pthreads \
                            --enable-pp \
                            --enable-liba52 \
                            --enable-x264 \
                            --enable-xvid \
                            --enable-libfaad \
                            --enable-libfaac \
                            --enable-libvorbis \
                            --enable-libmp3lame \
                            --enable-libogg \
                            --enable-libdts \
                            --enable-amr_nb-fixed \
                            --enable-amr_wb \
                            --enable-dc1394 \
                            --enable-libtheora \
                            --enable-shared \
                            --enable-x11grab \
                            --enable-libgsm \
                            --disable-static \
                            --disable-ffserver \
                            --disable-debug")

def build():
    autotools.make()
    autotools.make("cws2fws")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dobin("cws2fws")

    pisitools.dodoc("Changelog", "README", "doc/*.txt")
    pisitools.dohtml("doc/faq.html", "doc/ffmpeg-doc.html", "doc/ffplay-doc.html", "doc/hooks.html")

