#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    #autotools.autoreconf()
    #shelltools.export("CFLAGS","-O2 -g")
    #shelltools.export("CXXFLAGS","-O2 -g")
    autotools.configure("--enable-avahi \
                         --enable-oggvorbis")

def build():

    #shelltools.export("CC", "%s -lpthread -logg" %get.CFLAGS())
    autotools.make('CFLAGS="%s -lpthread -lz  -lgdbm -lid3tag -lavahi-client" LDFLAGS="%s" ' % (get.CFLAGS(), get.LDFLAGS()))

def install():
    autotools.install()
    pisitools.insinto("/etc","contrib/mt-daapd.playlist")

