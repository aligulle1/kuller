#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "%s-3.2.0.beta2" % get.srcNAME()

def setup():
    shelltools.export("TOPDIR", "%s/%s" % (get.workDIR(), WorkDir))
    autotools.configure("--with-zlib \
                         --with-proj \
                         --with-expat")

def build():
    shelltools.export("LD_LIBRARY_PATH", "%s/%s/bin/linux" % (get.workDIR(),get.srcDIR()))
    shelltools.export("TOPDIR", "%s/%s" % (get.workDIR(), WorkDir))
    autotools.make("-j1")

def install():
    shelltools.export("TOPDIR", "%s/%s" % (get.workDIR(), WorkDir))
    autotools.install()
    pisitools.dobin("ogdi-config")
    pisitools.insinto("/usr/lib/pkgconfig", "ogdi.pc")

    pisitools.dodoc("ChangeLog", "HOWTO-RELEASE", "LICENSE", "NEWS", "README", "README-BIN.TXT")
