#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    # dont compile samples
    pisitools.dosed("Makefile.in", "sample")
    autotools.configure("--disable-static")

def build():
    # u really suck
    shelltools.export("LC_ALL", "C")
    autotools.make("-j1")

def install():
    autotools.install()
    pisitools.dodoc("ChangeLog", "README*")
