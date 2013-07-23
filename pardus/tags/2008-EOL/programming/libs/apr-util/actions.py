#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--with-apr=/usr \
                         --includedir=/usr/include/apr-1 \
                         --without-gdbm \
                         --with-sqlite3 \
                         --with-berkeley-db \
                         --without-sqlite2 \
                         --enable-dbd-dso \
                         --disable-static")

def build():
    autotools.make()

def check():
    autotools.make("test")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # Not used
    pisitools.remove("/usr/lib/aprutil.exp")

    pisitools.dosed("%s/usr/bin/apu-1-config" % get.installDIR(), get.workDIR(), "")

    pisitools.dodoc("CHANGES", "NOTICE")
