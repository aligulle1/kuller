#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir="."

def install():
    shelltools.chmod("*.ttf",0644)
    shelltools.chmod("*.txt",0644)

    pisitools.insinto("/usr/share/fonts/dustin/","*.ttf")

    pisitools.dodoc("*.txt")