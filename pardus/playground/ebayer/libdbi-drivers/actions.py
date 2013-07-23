#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

WorkDir = "libdbi-drivers-0.8.3-1"

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools

def setup():
    shelltools.system("./autogen.sh")
    autotools.configure("--disable-static --with-mysql --with-pgsql --with-sqlite3 --disable-docs")

def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.removeDir("/usr/share")

