#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("build/mak/compiler/gcc.mak", "^GCC.CFLAGS.release.*$", "GCC.CFLAGS.release = ")
    pisitools.dosed("build/mak/compiler/gcc.mak", "^GCC.CXXFLAGS = \$.*$", "GCC.CXXFLAGS = $(GCC.CFLAGS)")

    autotools.rawConfigure("--prefix=/%s --mode=release --staticlibs=NO --target=..generic" % get.defaultprefixDIR())
    pisitools.dosed("config.mak", "CONF_DOCDIR=.*", "CONF_DOCDIR=/usr/share/doc/lensfun/")

def install():
    autotools.install("INSTALL_PREFIX=%s V=1" % get.installDIR())

