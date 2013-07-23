#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "gccxml"

def setup():
    cmaketools.configure("-DCMAKE_INSTALL_PREFIX=%s/usr \
                          -DCMAKE_CXX_COMPILER:FILEPATH=/usr/bin/g++ \
                          -DCMAKE_CXX_FLAGS=%s \
                          -DCMAKE_C_COMPILER:FILEPATH=/usr/bin/gcc \
                          -DCMAKE_C_FLAGS=%s" % (get.installDIR(), get.CXXFLAGS(), get.CFLAGS()))

def build():
    cmaketools.make()

def install():
    cmaketools.install()

