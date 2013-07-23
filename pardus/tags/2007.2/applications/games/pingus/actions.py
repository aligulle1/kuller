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
    # shelltools.unlink("po/tr.gmo")
    autotools.autoconf()

    shelltools.export("CXXFLAGS", "%s -I/usr/include/clanlib-0.6.5" % get.CXXFLAGS())
    shelltools.export("LDFLAGS", "%s -L/usr/lib/clanlib-0.6.5 -lclanCore -lclanApp" % get.LDFLAGS())

    autotools.configure('--with-bindir=/usr/bin \
                         --with-datadir=/usr/share/pingus \
                         --disable-nls \
                         --disable-rpath \
                         --with-clanGL')

def build():
    autotools.make()

def install():
    autotools.rawInstall('DESTDIR="%s"' % get.installDIR())
    pisitools.dodoc("AUTHORS", "NEWS", "README","TODO")

    pisitools.domove("/usr/games/", "/usr/bin")
    pisitools.domove("/usr/share/games/pingus", "/usr/share")
    pisitools.removeDir("/usr/share/games")

