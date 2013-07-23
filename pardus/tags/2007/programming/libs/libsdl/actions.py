#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005, 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import libtools
from pisi.actionsapi import get

WorkDir = "SDL-%s" % get.srcVERSION()

def setup():
    shelltools.system("./autogen.sh")

    autotools.configure("--enable-events \
                         --enable-cpuinfo \
                         --enable-cdrom \
                         --enable-threads \
                         --enable-timers \
                         --enable-endian \
                         --enable-file \
                         --enable-alsa \
                         --enable-esd \
                         --enable-arts \
                         --enable-nasm \
                         --enable-nas \
                         --enable-video-aalib \
                         --enable-video-caca \
                         --enable-video-directfb \
                         --enable-video-fbcon \
                         --enable-video-dummy \
                         --enable-video-opengl \
                         --enable-video-x11 \
                         --enable-video-x11-xv \
                         --enable-video-x11-xinerama \
                         --enable-video-x11-xrandr \
                         --with-x \
                         --disable-rpath \
                         --disable-dga \
                         --disable-video-dga \
                         --disable-video-ggi \
                         --disable-video-svga \
                         --disable-video-x11-xme \
                         --disable-dependency-tracking")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    libtools.preplib()

    pisitools.dosed("%s/usr/lib/libSDL.la" % get.installDIR(), "-pthread", " ")
    pisitools.dodoc("BUGS", "CREDITS", "README", "README-SDL.txt", "README.CVS", "TODO", "WhatsNew")
    pisitools.dohtml("./")

