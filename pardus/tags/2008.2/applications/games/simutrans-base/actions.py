#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools

import os

def fixperms(d):
    for root, dirs, files in os.walk(d):
        for name in dirs:
            shelltools.chmod(os.path.join(root, name), 0755)
        for name in files:
            shelltools.chmod(os.path.join(root, name), 0644)

WorkDir = "simutrans"
NoStrip = "/"

def install():
    fixperms("pak")
    pisitools.insinto("/usr/share/simutrans/pak", "pak/*")

    pisitools.dosym("/usr/share/simutrans/pak/text/en.tab", "/usr/share/simutrans/text/en.tab")
    pisitools.dosym("/usr/share/simutrans/pak/text/citylist_en_us.txt", "/usr/share/simutrans/text/citylist_en.txt")
