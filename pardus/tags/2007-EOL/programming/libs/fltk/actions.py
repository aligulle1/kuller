#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    cmaketools.configure("-DBUILD_EXAMPLES=OFF \
                          -DBUILD_SHARED_LIBS=ON \
                          -DBUILD_TESTING=OFF \
                          -DFLTK_USE_SYSTEM_JPEG=ON \
                          -DFLTK_USE_SYSTEM_PNG=ON \
                          -DFLTK_USE_SYSTEM_ZLIB=ON \
                          -DUSE_OPENGL=ON")

def build():
    cmaketools.make()

def install():
    cmaketools.install("DESTDIR=%s" % get.installDIR())

    pisitools.dosym("FLTK-1.1", "/usr/lib/fltk")

    pisitools.dosed("CMake/fltk-config", r"( *LIBS=.*)\.a(.*)", r"\1.so\2")
    pisitools.dobin("CMake/fltk-config")

    pisitools.dodoc("ANNOUNCEMENT", "CHANGES", "COPYING", "CREDITS", "README")

    pisitools.newman("documentation/fltk.man", "fltk.3")
    pisitools.newman("documentation/fltk-config.man", "fltk-config.1")
    pisitools.newman("documentation/fluid.man", "fluid.1")
