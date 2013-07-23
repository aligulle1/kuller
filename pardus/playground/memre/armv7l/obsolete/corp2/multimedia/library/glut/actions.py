#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import crosstools as autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def build():
    pisitools.dosed("src/glut/glx/Makefile", r"(^include\s*\$\(TOP\)/configs/).*", "\\1linux-fbdev")

    shelltools.cd("src/glut/glx")
    autotools.make('CC="%(CC)s" \
                    CFLAGS="%(CFLAGS)s -std=c99 -ffast-math -fexceptions -Wall -O3 -g -fPIC" \
                    LDFLAGS="%(LDFLAGS)s" \
                    X11_INCLUDES="-I%(RootDir)s/usr/include/X11" \
                    EXTRA_LIB_PATH="-L"%(RootDir)s/usr/lib' %
                    autotools.environment)

def install():
    pisitools.dodir("/usr/include")
    pisitools.dodir("/usr/lib")

    shelltools.copy("include/GL","%s/usr/include/GL" % get.installDIR())
    shelltools.copy("lib/*","%s/usr/lib/" % get.installDIR())

    pisitools.remove("/usr/lib/libglut.so")
    pisitools.remove("/usr/lib/libglut.so.3")
    pisitools.dosym("libglut.so.3","/usr/lib/libglut.so")
    pisitools.dosym("libglut.so.3.7.1","/usr/lib/libglut.so.3")
