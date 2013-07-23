#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "FOTAQ_Talkie"
NoStrip = "/"

datadir = "/usr/share/queen"

def install():
    pisitools.dodir(datadir)

    for f in ["queen.1c"]:
        shelltools.chmod(f, 0644)
        pisitools.insinto(datadir, f)

    pisitools.dodoc("readme.txt")

