#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007,2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get


def setup():
    pisitools.dosed("Makefile", "SUBDIRS=", "M=")
    pisitools.dosed("Makefile", "\$\(shell uname -r\)", get.curKERNEL())
    pisitools.dosed("Makefile", "`uname -r`", get.curKERNEL())

def build():
    autotools.make("KERNEL_DIR=/usr/src/linux-%s" % get.curKERNEL())

def install():
    pisitools.insinto("/lib/modules/%s/extra" % get.curKERNEL(), "*.ko")

    pisitools.dodoc("ChangeLog", "test/getjpeg.c")
