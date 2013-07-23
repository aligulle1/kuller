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


def setup():
    shelltools.export("CXXFLAGS", '%s -DEXPDATADIR=\\\"/usr/share/abuse_sdl/data\\\"' % get.CXXFLAGS())
    pisitools.dosed("src/sdlport/setup.cpp", "/usr/local/share/games/abuse", "/usr/share/abuse_sdl/data") 
    autotools.configure("--datadir=/usr/share/abuse_sdl/data")

def build():
    autotools.make()

def install():
    autotools.rawInstall('DESTDIR="%s"' % get.installDIR())
    pisitools.dodoc("AUTHORS", "ChangeLog", "TODO", "README")

