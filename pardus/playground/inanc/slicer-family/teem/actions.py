#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import get
from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools

WorkDir = "teem-1.9.0-src"

def setup():
    cmaketools.configure("-DBUILD_SHARED_LIBS=ON")

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s root=%s" % (get.installDIR(), get.installDIR()))

    pisitools.insinto("/usr/include", "include/*.h")
    pisitools.insinto("/usr/lib", "bin/libcoil.so")
    pisitools.insinto("/usr/lib", "bin/libhoover.so")
    pisitools.insinto("/usr/lib", "bin/libmite.so")
    pisitools.insinto("/usr/lib", "bin/libmoss.so")
    pisitools.insinto("/usr/lib", "bin/libpush.so")

    pisitools.insinto("/usr/lib/TEEM-1.9/", "CMake/*.cmake")
    pisitools.insinto("/usr/lib/TEEM-1.9/", "CMake/*.in")
