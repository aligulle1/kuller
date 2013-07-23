#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

shelltools.export("HOME", get.installDIR())
shelltools.export("AUTOPOINT", "/bin/true")

def setup():
    shelltools.system("./bootstrap")

    autotools.autoreconf("-vfi")
    pisitools.dosed("configure", "-ldts" , "-ldca")
    # dvdcss is handled via dlopen if disabled.
    # faac is always handled via libavcodec
    autotools.configure("--disable-debug \
                         --enable-ccache \
                         --disable-profiling \
                         --disable-optimizations \
                         --enable-gl \
                         --enable-vdpau \
                         --enable-vaapi \
                         --enable-xrandr \
                         --enable-pulse \
                         --enable-ffmpeg-libvorbis \
                         --disable-faac \
                         --disable-dvdcss \
                         --enable-external-ffmpeg \
                         --enable-external-python \
                         --disable-crystalhd \
                         --disable-vdadecoder \
                         --disable-joystick \
                         --enable-non-free \
                         --enable-external-libraries")

def build():
    autotools.make()
    autotools.make("-C tools/EventClients wiimote")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    autotools.rawInstall("DESTDIR=%s -C tools/EventClients" % get.installDIR())

    pisitools.doman("docs/manpages/*")
    pisitools.dodoc("*.txt", "README.linux", "LICENSE.GPL")

    pisitools.dosym("/usr/share/icons/hicolor/256x256/apps/xbmc.png", "/usr/share/pixmaps/xbmc.png")
