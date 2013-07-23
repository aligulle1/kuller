#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "crystalspace-src-%s" % get.srcVERSION()

def setup():
    autotools.configure("--disable-static-baselibs \
                         --enable-cpu-specific-optimizations=no \
                         --enable-optimize \
                         --disable-debug \
                         --disable-separate-debug-info \
                         --enable-ptmalloc \
                         --disable-extensive-memory-debugger \
                         --disable-ref-tracker \
                         --with-java \
                         --with-python \
                         --with-mesa \
                         --with-z \
                         --with-png \
                         --with-jpeg \
                         --with-lcms \
                         --with-mng \
                         --with-mikmod \
                         --with-ogg \
                         --with-vorbis \
                         --with-3ds \
                         --with-ode \
                         --with-freetype2 \
                         --with-cal3d \
                         --with-sdl \
                         --with-wx \
                         --with-CEGUI \
                         --with-Cg \
                         --with-CgGL \
                         --with-asound \
                         --with-caca \
                         --with-bfd")

def build():
    pisitools.dosed("Jamconfig", "-O3", get.CFLAGS())
    pisitools.dosed("Jamconfig", "/usr/local/lib", "/usr/lib")

    autotools.make()

def install():
    autotools.install()

    for files in ["cspace.py", "_cspace.so", "pycscegui.py", "_pycscegui.so"]:
        pisitools.domove("/usr/share/crystalspace-1.2/bindings/python/%s" % files, "/usr/lib/%s/site-packages/" % get.curPYTHON())

    pisitools.dosed("%s/etc/crystalspace-1.2/vfs.cfg" % get.installDIR(), get.installDIR())

    pisitools.rename("/usr/share/doc/crystalspace-1.2", get.srcTAG())
