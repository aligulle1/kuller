#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005, 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "SDL_mixer-%s" % get.srcVERSION()

def setup():
    pisitools.dosed("timidity/config.h", "/usr/local/lib/timidity", "/usr/share/timidity")
    autotools.configure("--disable-dependency-tracking \
                         --enable-music-mod \
                         --enable-timidity-midi \
                         --enable-music-libmikmod \
                         --enable-music-mp3 \
                         --enable-music-ogg")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("CHANGES", "COPYING", "README")
