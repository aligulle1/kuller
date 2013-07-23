#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

shelltools.export("HOME", get.workDIR())

def install():
    shelltools.chmod("*.ttf",0644)

    pisitools.insinto("/usr/share/fonts/gentium","*.ttf")

    pisitools.dodoc("NOTICE", "README.txt")
    pisitools.dodoc("DOCUMENT", "DOCUMENTATION.txt")
