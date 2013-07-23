#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("Makefile", "SUBDIRS=", "M=")
    pisitools.dosed("Makefile", "\$\(shell uname -r\)", get.curKERNEL())
    shelltools.chmod("example/*", 0644)

def build():
    autotools.make("KERNELDIR=/lib/modules/%s/build default" % get.curKERNEL())

def install():
    pisitools.insinto("/lib/modules/%s/extra" % get.curKERNEL(), "*.ko")
    pisitools.insinto("%s/%s/" % (get.docDIR(), get.srcTAG()), "example")

    pisitools.dodoc("COPYING", "README")
    pisitools.dohtml("*.html")
