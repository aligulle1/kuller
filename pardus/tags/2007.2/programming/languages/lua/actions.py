#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005, 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get


def setup():
    pisitools.dosed("config", "^#(LOADLIB= -DUSE_DLOPEN=1)", r"\1")
    pisitools.dosed("config", "^#(DLLIB= -ldl)", r"\1")
    pisitools.dosed("config", "^#(POPEN= -DUSE_POPEN=1)$", r"\1")
    pisitools.dosed("config", "^(MYCFLAGS= )-O2", r"\1%s -fPIC -DPIC" % get.CFLAGS())

def build():
    autotools.make()
    autotools.make("so sobin")

def install():
    pisitools.dodir("/usr/lib")
    autotools.rawInstall("DESTDIR=%s INSTALL_ROOT=%s/usr soinstall" % (get.installDIR(), get.installDIR()))

    pisitools.dodoc("HISTORY", "UPDATE")
    pisitools.dohtml("doc/*")

    pisitools.newdoc("etc/README", "README.etc")
    pisitools.newdoc("src/luac/README", "README.luac")
    pisitools.newdoc("src/lib/README", "README.lib")
    pisitools.newdoc("src/lua/README", "README.lua")
    pisitools.newdoc("test/README", "README.test")
    pisitools.dodoc("README")

    pisitools.insinto("/usr/share/lua", "etc/compat.lua")
    pisitools.insinto("/usr/share/pixmaps", "etc/lua.xpm")
    pisitools.insinto("/usr/lib/pkgconfig", "etc/lua.pc")
