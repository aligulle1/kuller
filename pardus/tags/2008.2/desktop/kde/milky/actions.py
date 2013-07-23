#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def install():
    pisitools.dodir("/usr/share/icons/Milky")

    for dir in ("128x128", "64x64", "48x48", "32x32", "22x22", "16x16"):
        shelltools.copytree(dir, "%s/usr/share/icons/Milky/%s" % (get.installDIR(), dir))

    for f in ["author", "index.theme", "license.txt", "readme.txt", "thanks.to"]:
        pisitools.insinto("/usr/share/icons/Milky", f)

