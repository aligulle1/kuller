#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import kerneltools
from pisi.actionsapi import get

WorkDir = "icebox-%s" % get.srcVERSION()
KVERSION = kerneltools.getKernelVersion()

def setup():
    pisitools.dosed("src/Makefile", "\$\(shell uname -r\)", KVERSION)

def build():
    autotools.make()

def install():
    pisitools.insinto("/lib/modules/%s/extra" % KVERSION, "src/*.ko")

    pisitools.dodoc("README", "AUTHORS", "ChangeLog", "COPYING")

