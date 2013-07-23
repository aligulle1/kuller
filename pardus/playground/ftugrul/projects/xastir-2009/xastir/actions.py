#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    autotools.autoreconf("-fi")
    autotools.configure("--with-ax25 \
                         --with-geotiff=/usr/include/libgeotiff \
                         --without-graphicsmagick")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("ABOUT-NLS", "AUTHORS", "COPYING", "COPYING.LIB.LESSTIF", "ChangeLog", "DEBUG_LEVELS", "FAQ", "INSTALL", "LICENSE", "NEWS", "README", "README.CVS", "README.Contributing", "README.Getting-Started", "README.MAPS", "UPGRADE")
