#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import shelltools
from pisi.actionsapi import scons
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "boswars-%s-src" % get.srcVERSION()

datadir="/usr/share/boswars"

def fixperms(d):
    import os

    for root, dirs, files in os.walk(d):
        for name in dirs:
            shelltools.chmod(os.path.join(root, name), 0755)
        for name in files:
            shelltools.chmod(os.path.join(root, name), 0644)

def build():
    shelltools.export("CFLAGS", "%s `sdl-config --cflags`" % get.CFLAGS())
    shelltools.export("CXXFLAGS", "%s `sdl-config --cflags`" % get.CXXFLAGS())
    scons.make()

def install():
    pisitools.insinto(datadir, "boswars")

    for files in ["campaigns", "graphics", "languages", "maps", \
                  "scripts", "sounds", "units", "video"]:
        fixperms(files)

        shelltools.copytree(files, "%s/%s/" % (get.installDIR(), datadir))

    pisitools.dodoc("CHANGELOG", "*.txt", "doc/*.txt")
    pisitools.dohtml("doc/*", "doc/scripts/*")
    pisitools.insinto("/usr/share/doc/%s/scripts" % get.srcTAG(), "doc/scripts/*.py")

