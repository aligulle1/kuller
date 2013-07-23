#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.export("CC", get.CC())
    shelltools.export("CXX", get.CXX())
    # Use secure delete. Even if the data is deleted with sqlite query, the traces of the deleted data still remains in the file
    # but cannot be seen with sqlite query. However, it can be seen by opening the file with a text editor.
    # SQLITE_SECURE_DELETE overwrites written data with zeros.
    shelltools.export("CFLAGS","%s \
                                -DSQLITE_SECURE_DELETE=1 \
                                -O3" % get.CFLAGS())

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
