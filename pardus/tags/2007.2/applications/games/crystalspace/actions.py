#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "crystalspace"

def setup():
    autotools.configure("--with-java \
                         --with-python \
                         --enable-cpu-specific-optimizations=no \
                         --disable-separate-debug-info \
                         --disable-debug \
                         --with-x \
                         --with-xaw7 \
                         --with-xxf86vm \
                         --with-mesa \
                         --with-CEGUI \
                         --with-z \
                         --with-png \
                         --with-jpeg \
                         --with-wx \
                         --with-Cg \
                         --with-CgGL \
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
                         --with-asound \
                         --with-caca \
                         --without-bfd \
                         --with-js=/opt/sun-jdk/jre/lib/i386")

def build():
    pisitools.dosed("Jamconfig", "-O3", get.CFLAGS())
    pisitools.dosed("Jamconfig", "/usr/local/lib", "/usr/lib")

    shelltools.system("jam")

def install():
    for f in ("install_bin", "install_plugin", "install_lib",
              "install_include", "install_data", "install_config", "install_doc"):
        shelltools.system("jam -s DESTDIR=%s %s" % (get.installDIR(), f))

    pisitools.domove("/%s/crystalspace/*" % get.docDIR(), "/%s/%s" % (get.docDIR(), get.srcTAG()))
    pisitools.removeDir("/%s/crystalspace" % get.docDIR())
    pisitools.dodoc("INSTALL", "LICENSE", "README")
