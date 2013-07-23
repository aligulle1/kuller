#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import get

WorkDir = "jvgs-%s-src" % get.srcVERSION()
resources_dir = "/usr/share/jvgs/resources"

def setup():
    cmaketools.configure()

def build():
    cmaketools.make()
    autotools.make()

def install():
    pisitools.dobin("src/jvgs")

    for data in ("resources/clock", "resources/common-scripts", "resources/effects", "resources/grenade", "resources/hat", "resources/hedgehog", "resources/helidude", "resources/knife", "resources/level-city", "resources/level-contact", "resources/level-credits", "resources/level-end", "resources/level-four", "resources/level-intro", "resources/level-knife", "resources/level-main-menu", "resources/level-nostalgia", "resources/level-planet", "resources/level-run", "resources/level-sea", "resources/modules", "resources/mouse", "resources/music", "resources/pacman", "resources/plant", "resources/player", "resources/spider", "resources/spikey-ball", "resources/velociraptor"):
        shelltools.copytree(data, "%s/%s" % (get.installDIR(), resources_dir))

    for files in ["resources/drawing.svg", "resources/font.ttf"]:
        pisitools.insinto(resources_dir, files)

    pisitools.insinto("/usr/share/jvgs/resources", "main.lua")

    pisitools.dodoc("AUTHORS", "README.markdown")

