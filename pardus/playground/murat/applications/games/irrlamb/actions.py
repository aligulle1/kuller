#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import scons
from pisi.actionsapi import get

WorkDir = "irrlamb"

datadir = "/usr/share/irrlamb"

def build():
    shelltools.unlinkDir("libraries")

    scons.make()

def install():
    pisitools.dobin("irrlamb")
    pisitools.rename("/usr/bin/irrlamb", "irrlamb.bin")

    pisitools.dodir(datadir)
    for data in ["art", "campaigns", "fonts", "levels", "meshes",
                 "scenes", "scripts", "sounds", "terrain", "textures"]:
        shelltools.copytree(data, "%s/%s" % (get.installDIR(), datadir))

    pisitools.dodoc("*.txt")
