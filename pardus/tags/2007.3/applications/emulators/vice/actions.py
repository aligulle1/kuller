#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--enable-textfield \
                         --disable-zlibtest \
                         --with-sdl \
                         --enable-fullscreen \
                         --disable-gnomeui \
                         --enable-realdevice \
                         --enable-ffmpeg \
                         --enable-ethernet \
                         --enable-ipv6 \
                         --enable-parsid \
                         --with-xaw3d \
                         --with-readline \
                         --with-alsa \
                         --without-esd \
                         --with-resid \
                         --with-png \
                         --with-zlib \
                         --with-picasso96")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dohtml("doc/html/*.html")
    pisitools.insinto("/%s/%s/html/images" % (get.docDIR(), get.srcTAG()), "doc/html/images/*")
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "FEEDBACK", "NEWS", "README", "doc/*.txt", "doc/html/plain/*")
