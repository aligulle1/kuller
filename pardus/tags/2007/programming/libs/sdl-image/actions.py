#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005, 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "SDL_image-1.2.5"

def setup():
    autotools.configure("--disable-dependency-tracking \
                         --enable-gif \
                         --enable-jpeg \
                         --enable-tif \
                         --enable-png \
                         --enable-pnm \
                         --enable-bmp \
                         --enable-xcf \
                         --enable-xpm \
                         --enable-tga \
                         --enable-lbm \
                         --enable-pcx")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dobin(".libs/showimage")
    pisitools.dodoc("CHANGES", "COPYING", "README")
