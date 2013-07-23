#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import kerneltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

KVERSION = kerneltools.getKernelVersion()

WorkDir = "ipheth"

def setup():
    pisitools.dosed("ipheth-driver/Makefile", "KVERSION =.*$", "KVERSION = %s" % KVERSION)

def build():
    autotools.make("-j1 -C ipheth-driver/")

def install():
    pisitools.insinto("/lib/modules/%s/extra" % KVERSION, "ipheth-driver/ipheth.ko")
