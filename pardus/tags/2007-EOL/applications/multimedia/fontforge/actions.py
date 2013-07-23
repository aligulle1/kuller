#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005, 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "fontforge-20061025"

def setup():
    pisitools.dosed("configure", "ungif", "gif")
    pisitools.dosed("gdraw/gimagereadgif.c", "libungif", "libgif")
    autotools.configure("--enable-extra-encodings \
                         --with-multilayer \
                         --without-freetype-src \
                         --with-x")

def build():
    autotools.make()

def install():
    autotools.install("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("AUTHORS", "README*")
