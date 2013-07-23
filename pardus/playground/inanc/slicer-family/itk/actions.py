#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import get
from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir = "InsightToolkit-%s" % get.srcVERSION()

shelltools.export("LD_LIBRARY_PATH", "/usr/lib")

def setup():
    cmaketools.configure("-DBUILD_SHARED_LIBS:BOOL=ON \
                          -DBUILD_EXAMPLES:BOOL=ON \
                          -DCMAKE_VERBOSE_MAKEFILE=OFF\
                          -DBUILD_EXAMPLES=OFF\
                          -DBUILD_TESTING=OFF\
                          -DITK_USE_REVIEW:BOOL=OFF \
                          -DITK_USE_PATENTED:BOOL=OFF \
                          -DITK_USE_SYSTEM_TIFF=ON \
                          -DITK_USE_SYSTEM_PNG=ON \
                          -DITK_USE_SYSTEM_ZLIB=ON \
                          -DITK_USE_SYSTEM_LIBXML2=ON \
                          -DUSE_FFTWD=ON")

def build():
    cmaketools.make("-j1")

def install():
    cmaketools.rawInstall("DESTDIR=%s root=%s" % (get.installDIR(), get.installDIR()))
