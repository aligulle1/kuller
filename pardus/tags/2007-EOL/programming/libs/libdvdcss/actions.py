#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2005, 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import libtools

def setup():
    autotools.autoreconf()
    libtools.libtoolize("--copy --force")

    # These flags do not bork on x86 ! Try and find out
    # shelltools.export("CFLAGS", "")
    # shelltools.export("CXXFLAGS", "")

    autotools.configure("--disable-static \
                         --disable-doc \
                         --disable-dependency-tracking")

def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.dodoc("ChangeLog", "AUTHORS", "NEWS", "README")
    pisitools.dohtml("doc/*.html")
    pisitools.dosym("libdvdcss.so.2.0.8", "/usr/lib/libdvdcss.so.0")
    pisitools.dosym("libdvdcss.so.2.0.8", "/usr/lib/libdvdcss.so.1")
