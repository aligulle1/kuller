#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006  TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "psqlodbc-08.02.0200"

def setup():
    autotools.configure("--with-unixodbc")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.rename("/usr/lib/psqlodbcw.so", "psqlodbc.so")
    pisitools.remove("/usr/lib/psqlodbcw.la")
    pisitools.dodoc("license.txt", "readme.txt")
