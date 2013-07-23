#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools

def setup():
    autotools.autoconf()

    shelltools.makedirs("build-ansi")
    shelltools.makedirs("build-unicode")
    shelltools.sym("../configure", "build-ansi/configure")
    shelltools.sym("../configure", "build-unicode/configure")

    shelltools.cd("build-ansi")
    autotools.configure("--with-png \
                         --with-jpeg \
                         --with-tiff \
                         --with-odbc \
                         --with-expat \
                         --with-opengl \
                         --with-sdl \
                         --enable-sound \
                         --enable-joystick \
                         --disable-unicode \
                         --enable-shared \
                         --with-gtk=2")

    shelltools.cd("../build-unicode")
    # it fails if ODBC is enabled when using unicode
    autotools.configure("--with-png \
                         --with-jpeg \
                         --with-tiff \
                         --with-expat \
                         --with-opengl \
                         --with-sdl \
                         --enable-sound \
                         --enable-joystick \
                         --enable-unicode \
                         --enable-xrc \
                         --enable-shared \
                         --with-gtk=2")

def build():
    shelltools.cd("build-ansi")
    autotools.make()
    autotools.make("-C contrib")
    shelltools.cd("../build-unicode")
    autotools.make()
    autotools.make("-C contrib")

def install():
    shelltools.cd("build-ansi")
    autotools.install()
    autotools.install("-C contrib")

    shelltools.cd("../build-unicode")
    autotools.install()
    autotools.install("-C contrib")
    shelltools.cd("..")

    pisitools.remove("/usr/bin/wx-config")
    pisitools.dosym("/usr/lib/wx/config/gtk2-unicode-release-2.6", "/usr/bin/wx-config")
    pisitools.dosym("/usr/lib/wx/config/gtk2-ansi-release-2.6", "/usr/bin/wx-config-ansi")
    pisitools.dodoc("docs/*.txt", "docs/*.htm")
