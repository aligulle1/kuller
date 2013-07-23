#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

import os

WorkDir = "."

def fixperms(d):
    for root, dirs, files in os.walk(d):
        for name in dirs:
            shelltools.chmod(os.path.join(root, name), 0755)
        for name in files:
            shelltools.chmod(os.path.join(root, name), 0644)

def build():
    autotools.make("BACKEND=sdl \
                    COLOUR_DEPTH=16 \
                    OSTYPE=linux \
                    OPTIMISE=2")

def install():
    pisitools.doexe("sim", "/usr/share/simutrans")

    for data in ("config", "font", "music", "text"):
        fixperms("simutrans/%s" % data)
        pisitools.insinto("/usr/share/simutrans", "simutrans/%s" % data)

    pisitools.remove("/usr/share/simutrans/text/en.tab")

    pisitools.dodoc("simutrans/*.txt", "documentation/*.txt")
