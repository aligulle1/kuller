#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "pySteg"

def install():
    pisitools.insinto("/usr/share/pysteg/data", "data/*")
    pisitools.insinto("/usr/share/pysteg/help", "help/*")
    pisitools.insinto("/usr/share/pysteg", "pysteg.py")

    pisitools.dosym("/usr/share/pysteg/data/pySteg_128.png", "/usr/share/pixmaps/pysteg.png")

    pisitools.dodoc("README", "LICENSE")
