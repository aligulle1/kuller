#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def build():
    autotools.make("BACKEND=sdl \
                    COLOUR_DEPTH=16 \
                    OSTYPE=linux \
                    OPTIMISE=2")

def install():
    pisitools.doexe("sim", "/usr/share/simutrans")

    pisitools.dodoc("*.txt", "documentation/*.txt")
