#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

WorkDir = "."

def setup():
    #autotools.autoreconf("-vif")
    autotools.configure("CXXFLAGS=\"$CXXFLAGS -fPIC\"")

def build():
    autotools.make()

def install():
    pisitools.dolib("libGLee.so")

    pisitools.insinto("/usr/include/GL", "GLee.h")

    pisitools.dodoc("extensionList.txt", "readme.txt")
