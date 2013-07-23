#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "fontforge-%s" % get.srcVERSION().split('_')[-1]

def setup():
    autotools.configure("--enable-devicetables \
                         --enable-libff \
                         --enable-pyextension \
                         --enable-type3 \
                         --with-regular-link \
                         --without-freetype-src \
                         --with-x")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.insinto("/usr/share/applications", "Packaging/fontforge.desktop")
    pisitools.insinto("/usr/share/pixmaps", "Packaging/fontforge.png")
    pisitools.insinto("/usr/share/mime/packages", "Packaging/fontforge.xml")

    pisitools.dodoc("AUTHORS", "LICENSE", "README*")

    shelltools.cd("pyhook")
    pythonmodules.install()
