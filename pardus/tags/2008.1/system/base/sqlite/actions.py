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
    shelltools.export("CFLAGS","%s -O3" % get.CFLAGS())
    shelltools.export("CXXFLAGS","%s -O3" % get.CXXFLAGS())

    autotools.configure("--enable-incore-db \
                         --enable-tempdb-in-ram \
                         --enable-threadsafe \
                         --disable-static \
                         --disable-tcl")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dobin("lemon")

    # docs
    pisitools.doman("sqlite3.1")
    pisitools.dodoc("README","VERSION")
