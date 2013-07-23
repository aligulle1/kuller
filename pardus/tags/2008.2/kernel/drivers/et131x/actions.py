#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "et131x-%s-3" % get.srcVERSION()
ksrc = "/lib/modules/%s/source" % get.curKERNEL()

def setup():
    pisitools.dosed("Makefile", "SUBDIRS=", "M=")
    pisitools.dosed("Makefile", "^KERNEL_VER :=.*", "KERNEL_VER := %s" % get.curKERNEL())
    pisitools.dosed("Makefile", "^KERNEL_64B :=.*", "KERNEL_64B := %s" % get.curKERNEL())

def build():
    autotools.make("KSRC=%s KERNEL_PATH=%s" % (ksrc, ksrc))

def install():
    pisitools.insinto("/lib/modules/%s/extra" % get.curKERNEL(), "*.ko")
    pisitools.dodoc("README.doc", "TODO", "MODULE-PARAMETER.txt")

