#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005, 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "%s+-%s" % (get.srcNAME(), get.srcVERSION())

def setup():
    pisitools.dosed("config.h", "#define SERIAL_CONSOLE_DEFAULT 0", "#define SERIAL_CONSOLE_DEFAULT 1")

def build():
    autotools.make()

def install():
    pisitools.insinto("/boot", "memtest.bin")
    pisitools.dodoc("FAQ", "README*")

