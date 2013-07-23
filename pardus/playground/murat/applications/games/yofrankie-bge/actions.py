#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
import os

NoStrip = ["/"]
WorkDir = "blender_game_engine"

datadir = "/usr/share/yofrankie-bge"
data = ["audio", "chars", "effects", "hud", "levels", "menus", "props", "textures"]

def fixperms(d):
    for root, dirs, files in os.walk(d):
        for name in dirs:
            shelltools.chmod(os.path.join(root, name), 0755)
        for name in files:
            shelltools.chmod(os.path.join(root, name), 0644)

def setup():
    fixperms(get.workDIR())

def install():
    for dirs in data:
        pisitools.insinto(datadir, dirs)

    pisitools.dodoc("yofrankie-DVD-license.txt")
