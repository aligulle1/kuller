#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006,2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get


def setup():

    shelltools.export("CFLAGS","%s -ffast-math -fPIC" % get.CFLAGS())
    shelltools.export("CXXFLAGS","%s -ffast-math -fPIC" % get.CFLAGS())

    autotools.configure("--enable-soname \
                         --enable-release \
                         --disable-double-precision \
                         --enable-opcode \
                         --enable-gyroscopic")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # No static libs
    pisitools.remove("/usr/lib/*.a")

    pisitools.dodoc("CHANGELOG.txt", "README.txt")
    pisitools.dohtml("docs/*")
