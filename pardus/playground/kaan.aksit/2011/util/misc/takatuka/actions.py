#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2011 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules

def install():
    pythonmodules.install()
    pisitools.dosym("/usr/share/takatuka/takatuka.py", "/usr/bin/takatuka")
    pisitools.dodoc("README","AUTHORS","COPYING")