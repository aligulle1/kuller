#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "zr364xx-0.64-fix1"

def setup():
    pisitools.dosed("Makefile", "SUBDIRS=", "M=")
    pisitools.dosed("Makefile", "^VERSION.*", "VERSION = %s" % get.curKERNEL())
    pisitools.dosed("Makefile", "/kernel/drivers/media/video", "/kernel/extra")

def build():
    autotools.make("KERNELDIR=/usr/src/linux-%s default" % get.curKERNEL())

def install():
    pisitools.insinto("/lib/modules/%s/extra" % get.curKERNEL(), "*.ko")

    pisitools.dodoc("CHANGELOG", "COPYING", "README")
