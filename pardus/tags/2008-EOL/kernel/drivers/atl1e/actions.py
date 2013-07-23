#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "atl1e-%s/src" % get.srcVERSION()

def build():
    pisitools.dosed("../atl1e.7", "arl1e", "atl1e")
    pisitools.dosed("Makefile", "/kernel/drivers/net/atl1e", "/extra")

    shelltools.export("KBUILD_NOPEDANTIC","1")
    autotools.make("-j1")

def install():
    shelltools.export("INSTALL_MOD_PATH", get.installDIR())
    shelltools.export("BUILD_KERNEL", get.curKERNEL())

    autotools.install()

    pisitools.dodoc("../copying", "../readme", "../ldistrib.txt")

