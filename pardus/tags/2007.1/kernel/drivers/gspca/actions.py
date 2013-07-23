#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "gspcav1-%s" % get.srcVERSION().split("_", 1)[1]

def setup():
    pisitools.dosed("Makefile", "SUBDIRS=", "M=")

def build():
    autotools.make("KERNELDIR=/usr/src/linux default")

def install():
    pisitools.insinto("/lib/modules/%s/extra" % get.curKERNEL(), "*.ko")
    pisitools.dodoc("changelog")

