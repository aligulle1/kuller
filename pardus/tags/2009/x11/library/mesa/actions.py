#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.autoreconf("-vif")
    autotools.configure("--enable-pic \
                         --disable-xcb \
                         --enable-glx-tls \
                         --disable-gl-osmesa \
                         --disable-egl \
                         --disable-glw \
                         --disable-glut \
                         --disable-gallium \
                         --with-driver=dri \
                         --with-dri-driverdir=/usr/lib/xorg/modules/dri")

def build():
    autotools.make("-j1")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # Create glxinfo/gears
    autotools.make("-C progs/xdemos glxinfo glxgears")

    pisitools.dobin("progs/xdemos/glxinfo")
    pisitools.dobin("progs/xdemos/glxgears")

    # Don't install unused headers
    for header in ("[a-fh-wyz]*.h", "gg*.h", "glf*.h", "*glut*.h"):
        pisitools.remove("/usr/include/GL/%s" % header)

    # Moving libGL for dynamic switching
    pisitools.domove("/usr/lib/libGL.so.1.2", "/usr/lib/mesa")

    pisitools.dodoc("docs/COPYING", "docs/enums.txt")
    pisitools.dohtml("docs/*")
