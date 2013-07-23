#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "scourge"

def setup():
    autotools.configure("--enable-sdl \
                         --enable-sdl_net \
                         --enable-sdl_mixer \
                         --disable-sdltest \
                         --enable-editor \
                         --with-data-dir=/usr/share/scourge")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.insinto("/usr/share/applications", "assets/scourge.desktop")
    pisitools.insinto("/usr/share/pixmaps", "assets/scourge.png")

    pisitools.rename("/usr/bin/tools", "scourge-tools")

    pisitools.dodoc("AUTHORS", "ChangeLog", "INSTALL", "NEWS", "README")
