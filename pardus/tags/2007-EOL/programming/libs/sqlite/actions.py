#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--enable-incore-db \
                         --enable-tempdb-in-ram \
                         --enable-threadsafe \
                         --enable-static=no \
                         --disable-tcl")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dobin("lemon")

    # docs
    pisitools.dodoc("README", "VERSION")
    pisitools.doman("sqlite3.1")
