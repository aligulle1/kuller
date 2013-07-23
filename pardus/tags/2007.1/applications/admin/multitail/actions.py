#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def build():
    autotools.make("all")

def install():
    pisitools.dobin("multitail")
    pisitools.insinto("/etc", "multitail.conf")

    pisitools.dodoc("Changes", "INSTALL", "license.txt", "readme.txt")
    pisitools.dohtml("manual*.html")
    pisitools.doman("multitail.1")

