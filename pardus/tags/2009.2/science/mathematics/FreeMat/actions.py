#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "%s-%s-Source" % (get.srcNAME(), get.srcVERSION())

def setup():
    pisitools.unlink("CMakeCache.txt")
    cmaketools.configure("-DUSE_LLVM=OFF")

def build():
    cmaketools.make()

def install():
    cmaketools.install("DESTDIR=%s" % get.installDIR())
    pisitools.insinto("/usr/share/pixmaps/", "images/freemat-2.xpm", "FreeMat.xpm")
    pisitools.remove("/usr/bin/blas.ini")
