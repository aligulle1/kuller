#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    autotools.configure("--enable-release \
                         --enable-shared \
                         --disable-static \
                         --enable-hal \
                         --enable-vlm \
                         --enable-sout \
                         --enable-live555 \
                         --enable-realrtsp \
                         --enable-dvdread \
                         --enable-dvdnav \
                         --enable-dvdplay \
                         --enable-smb \
                         --enable-dvbpsi \
                         --enable-v4l \
                         --enable-libcdio \
                         --enable-cddax \
                         --enable-libcddb \
                         --enable-vcdx \
                         --enable-vcd \
                         --enable-dvd \
                         --enable-dvb \
                         --enable-screen \
                         --enable-ogg \
                         --enable-mkv \
                         --enable-mpc \
                         --enable-mod \
                         --enable-mad \
                         --enable-avi \
                         --enable-asf \
                         --enable-ffmpeg \
                         --enable-xvid \
                         --enable-twolame \
                         --enable-a52 \
                         --enable-dts \
                         --enable-flac \
                         --enable-libmpeg2 \
                         --enable-vorbis \
                         --enable-speex \
                         --enable-theora \
                         --enable-png \
                         --enable-faad \
                         --enable-faac \
                         --enable-loader \
                         --enable-x11 \
                         --enable-xvideo \
                         --enable-glx \
                         --enable-xinerama \
                         --enable-opengl \
                         --enable-sdl \
                         --enable-freetype \
                         --enable-fribidi \
                         --enable-libxml2 \
                         --enable-svg \
                         --enable-skins2 \
                         --enable-alsa \
                         --enable-arts \
                         --enable-wxwidgets \
                         --disable-gnomevfs \
                         --disable-gtk \
                         --disable-daap \
                         --disable-bonjour \
                         --enable-lirc \
                         --enable-gnutls \
                         --enable-mozilla \
                         --with-libiconv=/usr \
                         --with-x \
                         --disable-jack \
                         --enable-dv \
                         --disable-snapshot \
                         --disable-growl \
                         --disable-pth \
                         --disable-portaudio \
                         --enable-x264 \
                         --enable-libtool \
                         --enable-mozilla=firefox \
                         --with-mozilla-sdk-path=/usr/lib/MozillaFirefox \
                         --enable-upnp")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("AUTHORS", "MAINTAINERS", "HACKING", "THANKS", "TODO", "NEWS", "README", "doc/fortunes.txt", "doc/intf-cdda.txt", "doc/intf-vcd.txt")

    for icon in ("128x128", "48x48", "32x32", "16x16"):
         pisitools.insinto("/usr/share/icons/hicolor/%s/apps/" % icon, "share/vlc%s.png" % icon, "vlc.png")
