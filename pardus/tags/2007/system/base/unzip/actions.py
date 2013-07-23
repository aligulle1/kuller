#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("unix/Makefile", "-O3", "%s " % get.CFLAGS())
    pisitools.dosed("unix/Makefile", "CC=gcc LD=gcc", "CC=%s LD=%s" % (get.CC(), get.CC()))
    pisitools.dosed("unix/Makefile", "-O ", "%s " % get.CFLAGS())

def build():
    autotools.make("-f unix/Makefile linux_noasm")

def install():
    for bin in ["unzip", "funzip", "unzipsfx", "unix/zipgrep"]:
        pisitools.dobin(bin)
    
    pisitools.dosym("/usr/bin/unzip", "/usr/bin/zipinfo")
    pisitools.doman("man/*.1")
    pisitools.dodoc("BUGS", "History*", "README", "ToDo", "WHERE")
