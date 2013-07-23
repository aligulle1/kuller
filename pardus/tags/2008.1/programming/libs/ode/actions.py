#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.export("CFLAGS","%s -fomit-frame-pointer -ffast-math -fPIC" % get.CFLAGS())
    shelltools.export("CXXFLAGS","%s -fomit-frame-pointer -ffast-math -fPIC" % get.CFLAGS())

    for f in ["NEWS", "README", "AUTHORS", "ChangeLog"]:
        shelltools.touch(f)

    autotools.autoreconf("-fi")
    autotools.configure("--enable-soname \
                         --enable-release \
                         --enable-double-precision \
                         --enable-opcode \
                         --enable-gyroscopic \
                         --disable-dependency-tracking")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # No static libs
    pisitools.remove("/usr/lib/*.a")

    pisitools.dodoc("CHANGELOG.txt", "README.txt")
    pisitools.dohtml("docs/*")
