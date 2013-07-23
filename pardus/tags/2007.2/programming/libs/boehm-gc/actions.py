#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "gc%s" % get.srcVERSION()

def setup():
    autotools.configure("--enable-cplusplus \
                         --disable-static")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.insinto("/usr/include/gc", "include/cord.h")
    pisitools.insinto("/usr/include/gc", "include/ec.h")
    pisitools.insinto("/usr/include/gc", "include/javaxfc.h")
    pisitools.insinto("/usr/include/gc/private", "include/private/*.h")

    pisitools.dodoc("README.QUICK", "doc/README*", "doc/barrett_diagram")
    pisitools.dohtml("doc/")
    pisitools.newman("doc/gc.man", "GC_malloc.1")
