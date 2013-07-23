#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.autoconf()
    autotools.configure("--with-expat \
                         --with-gtk=2 \
                         --with-jpeg \
                         --with-odbc \
                         --with-opengl \
                         --with-png \
                         --with-sdl \
                         --with-tiff \
                         --enable-display \
                         --enable-geometry \
                         --enable-graphics_ctx \
                         --enable-intl \
                         --enable-joystick \
                         --enable-mediactrl \
                         --disable-optimise \
                         --disable-rpath \
                         --enable-shared \
                         --enable-soname \
                         --enable-sound \
                         --enable-timer \
                         --enable-unicode \
                         --enable-xrc")

def build():
    autotools.make()
    autotools.make("-C contrib")
    autotools.make("-C locale allmo")

def install():
    autotools.install()
    autotools.install("-C contrib")

    pisitools.remove("/usr/bin/wx-config")
    pisitools.dosym("/usr/lib/wx/config/gtk2-unicode-release-2.8", "/usr/bin/wx-config")

    pisitools.dodoc("docs/*.txt", "docs/*.htm")
