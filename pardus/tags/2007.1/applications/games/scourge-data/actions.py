#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools

import os

WorkDir = "scourge_data"

def fixperms(d):
    for root, dirs, files in os.walk(d):
        for name in dirs:
            shelltools.chmod(os.path.join(root, name), 0755)
        for name in files:
            shelltools.chmod(os.path.join(root, name), 0644)

def setup():
    for data in ["cave", "icons", "maps", "objects", "sound", "themes", "world", "fonts", "mapgrid", "models", "portraits", "textures", "tools"]:
        fixperms(data)

def install():
    pisitools.insinto("usr/share/scourge", "*")