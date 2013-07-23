#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules

WorkDir = "Pyrex-0.9.4.1"

def install():
    pythonmodules.install()

    pisitools.dodoc("CHANGES.txt", "INSTALL.txt", "README.txt", "USAGE.txt")
    pisitools.dohtml("Doc/*")
