#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("Makefile", "(?m)^(CC.*)gcc", r"\1" + get.CC())
    pisitools.dosed("Makefile", "(?m)^(CFLAGS)-02", r"%s" % get.CFLAGS())

def build():
    autotools.make()

def install():
    pisitools.dosbin("hdparm", "/sbin")
    pisitools.dosbin("contrib/idectl", "/sbin")

    pisitools.doman("hdparm.8")
    pisitools.dodoc("hdparm.lsm", "Changelog", "README.acoustic", "hdparm-sysconfig")
