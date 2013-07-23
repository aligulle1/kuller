#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import get

WorkDir = "unrar"

def build():
    autotools.make("-f makefile.unix CXXFLAGS=\"%s\"" % get.CXXFLAGS())

def install():
    pisitools.insinto("/usr/bin", "unrar")

    pisitools.dodoc("readme.txt")

