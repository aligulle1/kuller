#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "scourge"

def setup():
    # Use wxWidgets-ansi
    pisitools.dosed("configure.in","wx-config","wx-config-ansi")

    autotools.autoreconf("-fi")

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

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README")
