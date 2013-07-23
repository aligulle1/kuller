#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import scons
from pisi.actionsapi import get
import os

resources_dir = "/usr/share/btanks"
lib_dir = "/usr/lib"

NoStrip = resources_dir

def fixperms(d):
    for root, dirs, files in os.walk(d):
        for name in dirs:
            shelltools.chmod(os.path.join(root, name), 0755)
        for name in files:
            shelltools.chmod(os.path.join(root, name), 0644)

def setup():
    pisitools.dosed("SConstruct", "-O3", get.CXXFLAGS())

def build():
    scons.make("prefix=/usr \
                resources_dir=%s \
                lib_dir=%s \
                enable_lua=no \
                mode=release" % (resources_dir, lib_dir))

def install():
    pisitools.dobin("bt")
    pisitools.rename("/usr/bin/bt", "btanks")

    pisitools.dolib_so("*.so")

    for files in ["data/*.xml", "data/playlist"]:
        pisitools.insinto(resources_dir, files)

    for data in ["data/font", "data/maps", "data/sounds", "data/tiles", "data/tilesets", "data/tunes"]:
        shelltools.copytree(data, "%s/%s" % (get.installDIR(), resources_dir))

    pisitools.dodoc("ChangeLog", "LICENSE", "*.txt")
