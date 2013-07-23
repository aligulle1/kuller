#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    #Link to ncurses, will be needed when we use as-needed ;)
    pisitools.dosed("support/shobj-conf", "^SHLIB_LIBS=", "SHLIB_LIBS=-lncurses")

    autotools.configure("--with-curses \
                         --libdir=/lib \
                         --disable-static")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s install" % get.installDIR())

    pisitools.dohtml("doc/")
    pisitools.dodoc("CHANGELOG", "CHANGES", "README", "USAGE", "NEWS")