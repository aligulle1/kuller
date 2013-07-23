#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005, 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    shelltools.export("WANT_AUTOCONF", "2.5")
    autotools.autoconf()
    autotools.configure("--libdir=/usr/lib \
                         --disable-static \
                         --enable-esd \
                         --enable-sdl \
                         --enable-alsa \
                         --enable-arts \
                         --enable-mp3 \
                         --enable-vorbis")

def build():
    autotools.make("-j1 all")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR()) 
    pisitools.dodoc("AUTHORS", "ChangeLog", "NEWS","NOTES", "README", "TODO")
