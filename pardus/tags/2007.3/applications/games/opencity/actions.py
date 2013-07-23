#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

datadir = "/usr/share/opencity"

WorkDir = "opencity-%sstable" % get.srcVERSION()
NoStrip = datadir

def setup():
    autotools.configure("--disable-sdltest \
                         --enable-sdl-mixer")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.domove("%s/OpenCity.desktop" % datadir, "/usr/share/applications")
    pisitools.domove("%s/OpenCity.png" % datadir, "/usr/share/pixmaps")

    for dirs in ["autopackage", "docs"]:
        pisitools.removeDir("%s/%s" % (datadir, dirs))

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "COPYRIGHT", "NEWS", "README", "TODO", "docs/FAQ.txt")
