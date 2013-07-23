#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "widelands"
datadir = "/usr/share/widelands"
NoStrip = [datadir]

def build():
    autotools.make()

def install():
    pisitools.dodir(datadir)

    pisitools.dobin("widelands")

    for data in ["campaigns", "fonts", "maps", "music", "pics", "sound", "tribes", "txts", "worlds"]:
        shelltools.copytree(data, "%s/%s" % (get.installDIR(), datadir))

    pisitools.insinto("/usr/share/pixmaps", "pics/wl-ico-64.png", "widelands.png")

    shelltools.copytree("locale", "%s/%s" % (get.installDIR(), datadir))

    pisitools.dohtml("doc/geometry/*.html", "doc/geometry/*.png")
    pisitools.dodoc("doc/README*", "ChangeLog", "COPYING", "CREDITS")
