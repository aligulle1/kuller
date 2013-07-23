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

import os

WorkDir = "mplayer-%s" % get.srcVERSION().split("_", 1)[1]
version = "23609"

def fixPermissions(dest):
    for root, dirs, files in os.walk(dest):
        for name in dirs:
            shelltools.chmod(os.path.join(root, name), 0755)
        for name in files:
            shelltools.chmod(os.path.join(root, name), 0644)

def setup():
    fixPermissions("DOCS")
    shelltools.export("LINGUAS", "tr")

    shelltools.unlink("version.sh")
    shelltools.echo("version.sh", '#!/bin/bash\necho "#define VERSION \\\"dev-SVN-r%s\\\"" > version.h' % version)
    shelltools.echo("version.sh", 'echo "#define MP_TITLE \\\"MPlayer dev-SVN-r%s (C) 2000-2007 MPlayer Team\\\" " >> version.h' % version)
    shelltools.chmod("version.sh", 0755)

    # let's try these flags and see if it borks
    # shelltools.export("CFLAGS", "%s -ffast-math -fomit-frame-pointer -D__STDC_LIMIT_MACROS" % get.CFLAGS())
    # shelltools.export("CXXFLAGS", "%s -ffast-math -fomit-frame-pointer -D__STDC_LIMIT_MACROS" % get.CXXFLAGS())
    shelltools.export("CFLAGS", "%s -ffast-math -fomit-frame-pointer" % get.CFLAGS())
    shelltools.export("CXXFLAGS", "%s -ffast-math -fomit-frame-pointer" % get.CXXFLAGS())

    autotools.rawConfigure('--prefix=/usr \
                         --confdir=/usr/share/mplayer \
                         --datadir=/usr/share/mplayer \
                         --disable-3dfx \
                         --disable-3dnow \
                         --disable-3dnowext \
                         --disable-altivec \
                         --disable-bitmap-font \
                         --disable-debug \
                         --disable-dvdread-internal \
                         --disable-ssse3 \
                         --disable-faad-external \
                         --disable-fribidi \
                         --disable-gcc-check \
                         --disable-ggi \
                         --disable-jack \
                         --disable-libdvdcss-internal \
                         --disable-mga \
                         --disable-svga \
                         --disable-tdfxfb \
                         --disable-tdfxvid \
                         --enable-aa \
                         --enable-alsa \
                         --enable-ass \
                         --enable-arts \
                         --enable-bl \
                         --enable-caca \
                         --enable-cdparanoia \
                         --enable-color-console \
                         --enable-dvb \
                         --enable-dvdnav \
                         --enable-dvdread \
                         --enable-esd \
                         --enable-fbdev \
                         --enable-freetype \
                         --enable-ftp \
                         --enable-gif \
                         --enable-gl \
                         --enable-gui \
                         --enable-inet6 \
                         --enable-joystick \
                         --enable-jpeg \
                         --enable-langinfo \
                         --enable-largefiles \
                         --enable-libamr_nb \
                         --enable-libamr_wb \
                         --enable-libcdio \
                         --enable-liblzo \
                         --enable-lirc \
                         --enable-mad \
                         --enable-mencoder \
                         --enable-menu \
                         --enable-mmx \
                         --enable-mmxext \
                         --enable-nas \
                         --enable-network \
                         --enable-ossaudio \
                         --enable-png \
                         --enable-radio \
                         --enable-radio-capture \
                         --enable-real \
                         --enable-rtc \
                         --enable-runtime-cpudetection \
                         --enable-cmov \
                         --enable-sdl \
                         --enable-shm \
                         --enable-smb \
                         --enable-sse \
                         --enable-tga \
                         --enable-tv \
                         --enable-tv-v4l1 \
                         --enable-tv-v4l2 \
                         --enable-unrarlib \
                         --enable-libvorbis \
                         --enable-win32dll \
                         --enable-x11 \
                         --enable-xf86keysym \
                         --enable-xinerama \
                         --enable-xshape \
                         --enable-xv \
                         --enable-xvmc \
                         --with-xvmclib=XvMCW \
                         --language=tr \
                         --charset=UTF-8 \
                         --codecsdir=/usr/lib/%(esdir)s \
                         --win32codecsdir=/usr/lib/%(esdir)s \
                         --xanimcodecsdir=/usr/lib/%(esdir)s \
                         --realcodecsdir=/usr/lib/%(esdir)s \
                         --disable-rpath' \
                         % {"esdir": "essential"})

                         # stuff that fail hede=yes check, but working with hede=auto
                         # --enable-directfb \
                         # --enable-fontconfig \
                         # --enable-xvid \
                         # --enable-theora \

    pisitools.dosed("config.mak", "GIF_LIB =", "GIF_LIB = -lungif")

def build():
    autotools.make("-j1")

def install():
    autotools.install("prefix=%(D)s/usr \
                       BINDIR=%(D)s/usr/bin \
                       LIBDIR=%(D)s/usr/lib \
                       CONFDIR=%(D)s/usr/share/mplayer \
                       DATADIR=%(D)s/usr/share/mplayer \
                       MANDIR=%(D)s/usr/share/man" % {"D": get.installDIR()})

    # set the default skin for gui
    shelltools.copytree("default_skin", "%s/usr/share/mplayer/skins/default" % get.installDIR())

    # codecs conf, not something user will interact with
    pisitools.insinto("/usr/share/mplayer", "etc/codecs.conf")

    # example dvb conf
    pisitools.insinto("/usr/share/mplayer", "etc/dvb-menu.conf")

    # just for fast access to conf
    pisitools.dosym("/etc/mplayer.conf", "/usr/share/mplayer/mplayer.conf")

    # install docs, tools, examples
    pisitools.dodoc("AUTHORS", "ChangeLog", "README")
    pisitools.insinto("/usr/share/doc/%s/" % get.srcTAG(), "TOOLS")
    pisitools.insinto("/usr/share/doc/%s/" % get.srcTAG(), "DOCS/tech")

    # we will use our own desktop file and icon
    pisitools.remove("/usr/share/applications/mplayer.desktop")
    pisitools.remove("/usr/share/pixmaps/mplayer.xpm")

