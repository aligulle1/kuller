#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "m5602"

def setup():
    pisitools.dosed("Makefile", "\$\(shell uname -r\)", get.curKERNEL())
    pisitools.dosed("Makefile", "SUBDIRS=", "M=")

def build():
    autotools.make('KDIR=/lib/modules/%s/build \
                    PWD="%s"' % (get.curKERNEL(), get.curDIR()))

def install():
    pisitools.insinto("/lib/modules/%s/extra" % get.curKERNEL(), "*.ko")

    pisitools.dodoc("COPYING", "README")
