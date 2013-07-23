#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2006-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("Makefile","DEPMOD  :=.*","DEPMOD := true")
    pisitools.dosed("Makefile", "/misc")

def build():
    autotools.make('all \
                    LINUX_DIR=/usr/src/linux-%s \
                    MODULE_OPT="%s -fomit-frame-pointer -fno-strict-aliasing -fno-common" \
                    PREFIX=%s/usr' % (get.curKERNEL(), get.CFLAGS(), get.installDIR()))

def install():
    autotools.rawInstall("all \
                          PREFIX=%s/usr \
                          MODULE_DIR=%s/lib/modules/%s/extra" % (get.installDIR(),get.installDIR(),get.curKERNEL()))

    pisitools.dodoc("COPYING", "CREDITS", "README*", "FAQ")

