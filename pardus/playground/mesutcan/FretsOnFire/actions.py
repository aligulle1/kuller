#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "Frets on Fire-%s" % get.srcVERSION()

def install():
    for i in ["data", "src"]:
        pisitools.insinto("/usr/share/FretsOnFire", i)

    pisitools.removeDir("/usr/share/FretsOnFire/data/win32")

    pisitools.insinto("/usr/share/pixmaps", "data/pose.png", "fretsonfire.png")

    pisitools.dodoc("copying.txt", "readme.txt", "todo.txt")
