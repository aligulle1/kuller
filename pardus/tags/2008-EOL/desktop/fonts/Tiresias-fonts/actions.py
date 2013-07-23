#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2008  TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="tiresias"

def install():
        pisitools.insinto("/usr/share/fonts/tiresias/", "*.ttf")
        pisitools.insinto("/usr/share/fonts/tiresias/", "*.TTF")
        shelltools.chmod("%s/usr/share/fonts/tiresias/*" % get.installDIR(), 0644)

        pisitools.dodoc("COPYING/*.doc", "COPYING/*.txt")
