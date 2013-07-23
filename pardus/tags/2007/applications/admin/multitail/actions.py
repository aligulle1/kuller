#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get 

def build():
    autotools.make("all")

def install():
    pisitools.dobin("multitail")
    pisitools.insinto("/etc", "multitail.conf")

    pisitools.dodoc("Changes", "INSTALL", "license.txt", "readme.txt")
    pisitools.dohtml("*.html")
    pisitools.doman("multitail.1")

