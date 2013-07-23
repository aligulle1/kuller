#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "ungrab-winmodem-20080126"

def setup():
    pisitools.dosed("Makefile", "SUBDIRS=\$(shell pwd)", "SUBDIRS=%s" % get.srcDIR())
    pisitools.dosed("Makefile", "SUBDIRS=", "M=")
    pisitools.dosed("Makefile", "^KERNEL_VER:=.*", "KERNEL_VER:= %s" % get.curKERNEL())

def build():
    autotools.make("KERNEL_DIR=/lib/modules/%s/build" % get.curKERNEL())

def install():
    pisitools.insinto("/lib/modules/%s/extra" % get.curKERNEL(), "*.ko")
    pisitools.dodoc("Readme.txt")

