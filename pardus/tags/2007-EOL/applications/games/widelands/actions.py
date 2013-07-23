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
NoStrip = datadir

def fixperms(d):
    import os
    for root, dirs, files in os.walk(d):
        for name in dirs:
            shelltools.chmod(os.path.join(root, name), 0755)
        for name in files:
            shelltools.chmod(os.path.join(root, name), 0644)

def build():
    autotools.make()

def install():
    pisitools.dodir(datadir)

    pisitools.dobin("widelands")

    for data in ["campaigns", "fonts", "maps", "music", "pics", "sound", "tribes", "txts", "worlds"]:
        fixperms(data)
        shelltools.unlink("%s/SConscript" % data)
        shelltools.copytree(data, "%s/%s" % (get.installDIR(), datadir))

    pisitools.insinto("/usr/share/pixmaps", "pics/wl-ico-64.png", "widelands.png")

    shelltools.system("python utils/buildlocale.py")
    shelltools.copytree("locale", "%s/%s" % (get.installDIR(), datadir))

    pisitools.dodoc("ChangeLog", "COPYING", "CREDITS")
