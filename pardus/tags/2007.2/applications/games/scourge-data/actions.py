#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

import os

WorkDir = "scourge_data"

def fixperms(d):
    for root, dirs, files in os.walk(d):
        for name in dirs:
            shelltools.chmod(os.path.join(root, name), 0755)
        for name in files:
            shelltools.chmod(os.path.join(root, name), 0644)

def install():
    pisitools.dodir("/usr/share/scourge")

    for data in ["cave", "config", "fonts", "icons", "mapgrid", "maps", "mod",
                 "models", "objects", "portraits", "script", "sound", "textures",
                 "themes", "tools", "world"]:
        fixperms(data)

        shelltools.copytree(data ,"%s/usr/share/scourge" % get.installDIR())
