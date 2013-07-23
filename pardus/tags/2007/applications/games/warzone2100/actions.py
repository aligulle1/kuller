#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "warzone-%s" % get.srcVERSION()

def setup():
    autotools.configure("--disable-dependency-tracking \
                         --with-ogg \
                         --with-mp3 \
                         --disable-debug")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("AUTHORS", "CHANGELOG", "README", "TODO")
    shelltools.chmod("debian/warzone2100.png", 0644)
    pisitools.insinto("/usr/share/pixmaps", "debian/warzone2100.png")
