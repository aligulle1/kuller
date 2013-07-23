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
    pisitools.dosed("src/Makefile", "CFLAGS= -O2", "CFLAGS= %s -fPIC -DPIC -DUSE_DLOPEN=1 -DUSE_POPEN=1" % get.CFLAGS())

def build():
    autotools.make("linux")

def install():
    autotools.rawInstall("INSTALL_TOP=%s/usr" % get.installDIR())

    pisitools.dosym("/usr/lib/liblua.so.5.1", "/usr/lib/liblua.so")

    pisitools.insinto("/usr/share/lua/5.1", "etc/strict.lua.lua")
    pisitools.insinto("/usr/share/lua/5.1", "test/*.lua")
    pisitools.insinto("/usr/lib/pkgconfig", "etc/lua.pc")

    pisitools.dohtml("doc")
    pisitools.newdoc("etc/README", "README.etc")
    pisitools.newdoc("test/README", "README.test")
    pisitools.dodoc("COPYRIGHT", "HISTORY", "README")
