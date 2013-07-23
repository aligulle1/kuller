#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

WorkDir = "L/src"

def build():
    autotools.make()

def install():
    pisitools.dobin("lcalc")
    pisitools.dolib_so("libLfunction.so")

    pisitools.insinto("usr/include/Lfunction","../include/*.h")

    pisitools.dodoc("../COPYING", "../README")
