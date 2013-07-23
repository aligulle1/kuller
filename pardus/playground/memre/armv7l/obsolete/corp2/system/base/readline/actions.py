#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import crosstools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    # Link to ncurses, will be needed when we use as-needed ;)
    pisitools.dosed("support/shobj-conf", r"^(SHLIB_LIBS\s*=.*)$", "\\1 -lncurses")

    crosstools.environment["CFLAGS"] = "%(CFLAGS)s -D_GNU_SOURCE" % crosstools.environment

    crosstools.autoconf()
    crosstools.configure("--with-curses \
                          --libdir=/lib \
                          --disable-static")

def build():
    crosstools.make()

def install():
    crosstools.rawInstall("DESTDIR=%s install" % get.installDIR())

    pisitools.dohtml("doc/")
    pisitools.dodoc("CHANGELOG", "CHANGES", "README", "USAGE", "NEWS")
