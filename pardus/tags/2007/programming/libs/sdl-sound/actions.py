#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005, 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "SDL_sound-1.0.1"

def setup():
    autotools.configure("--disable-dependency-tracking \
                         --disable-smpeg \
                         --enable-midi \
                         --enable-flac \
                         --enable-speex \
                         --enable-mikmod \
                         --enable-mpglib \
                         --enable-ogg")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("CHANGELOG", "CREDITS", "README", "TODO")
