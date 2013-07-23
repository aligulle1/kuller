#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007,2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    autotools.autoreconf("-fi")
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
                         --enable-dvb \
                         --enable-screen \
                         --enable-ogg \
                         --enable-mkv \
                         --enable-mpc \
                         --enable-mod \
                         --enable-mad \
                         --enable-ffmpeg \
                         --enable-twolame \
                         --enable-a52 \
                         --enable-dca \
                         --enable-flac \
                         --enable-libmpeg2 \
                         --enable-vorbis \
                         --enable-speex \
                         --enable-theora \
                         --enable-png \
                         --enable-faad \
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
                         --enable-pulse \
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
                         --enable-upnp")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    for icon in ("128x128", "48x48", "32x32", "16x16"):
         pisitools.insinto("/usr/share/icons/hicolor/%s/apps/" % icon, "share/vlc%s.png" % icon, "vlc.png")

    # Fix Firefox plugin location
    pisitools.rename("/usr/lib/mozilla","nsbrowser")
    pisitools.remove("/usr/lib/nsbrowser/plugins/*.la")

    pisitools.dodoc("AUTHORS", "THANKS", "NEWS", "README", "MAINTAINERS", "HACKING",
                    "doc/fortunes.txt","doc/intf-cdda.txt", "doc/intf-vcd.txt")

