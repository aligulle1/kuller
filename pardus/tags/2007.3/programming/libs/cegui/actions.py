#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "CEGUI-%s" % get.srcVERSION()

def setup():
    autotools.configure("--enable-xerces-c \
                         --enable-libxml \
                         --enable-expat \
                         --enable-tinyxml \
                         --enable-opengl-renderer \
                         --enable-tga \
                         --enable-samples \
                         --enable-toluacegui \
                         --with-x \
                         --with-gtk2")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "NEWS", "README")
