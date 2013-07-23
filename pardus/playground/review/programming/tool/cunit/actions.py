#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2011 TUBITAK/BILGEM
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

WorkDir = "CUnit-%s-2" % get.srcVERSION()

def setup():
    shelltools.export("LDFLAGS", "%s" % get.LDFLAGS())
    shelltools.export("CFLAGS", "%s" % get.CFLAGS())
    for file in ["doc/Makefile.am", "doc/headers/Makefile.am"]:
        pisitools.dosed(file, "\$\(prefix\)/doc/", "$(prefix)/share/doc/")
    autotools.autoreconf("-vfi")
    autotools.configure("--enable-examples")

def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.insinto("/usr/share/doc/CUnit/Examples", "Examples/*")
    pisitools.remove("/usr/lib/libcunit.a")

