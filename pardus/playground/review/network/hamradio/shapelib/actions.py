#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2011 TUBITAK/BILGEM
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("Makefile", "/usr/local/", "%s/usr/" % get.installDIR())
    pisitools.dosed("Makefile", "SHPLIB_VERSION=1.2.9", "SHPLIB_VERSION=1.2.10")

def build():
    autotools.make()
    autotools.make("lib")

def check():
    autotools.make("test")

def install():
    autotools.make("lib_install")

    pisitools.dobin("shpadd")
    pisitools.dobin("shpcreate")
    pisitools.dobin("shpdump")
    pisitools.dobin("shprewind")
    pisitools.dobin("shptest")
    pisitools.dobin("dbfadd")
    pisitools.dobin("dbfcreate")
    pisitools.dobin("dbfdump")

    pisitools.remove("/usr/lib/*.a")

    pisitools.dodoc("ChangeLog", "LICENSE.LGPL", "README", "README.tree")
