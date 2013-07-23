#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

import os

NoStrip = "/"

datadir = "/usr/share/eternal-lands"
data = ["2dobjects", "3dobjects", "actor_defs", "animations", "maps", "meshes",
        "mapeditor", "particles", "skeletons", "sound", "textures", "tiles",
        "languages"]


def fixperms(d):
    for root, dirs, files in os.walk(d):
        for name in dirs:
            shelltools.chmod(os.path.join(root, name), 0755)
        for name in files:
            shelltools.chmod(os.path.join(root, name), 0644)

def install():
    for files in ["3dobjects.txt", "e3dlist.txt", "global_filters.txt",
                  "*.lst", "*.xml"]:
        pisitools.insinto(datadir, files)

    for f in data:
        fixperms(f)
        shelltools.copytree(f, "%s/%s" % (get.installDIR(), datadir))

    pisitools.dodoc("license.txt")
    pisitools.dohtml("*.html")
