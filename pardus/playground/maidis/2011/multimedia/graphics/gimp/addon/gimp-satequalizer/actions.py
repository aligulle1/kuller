#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "satequalizer"

def build():
    shelltools.system("gimptool-2.0  --build saturate.c || exit 1")

def install():
    pisitools.dolib("saturate", "/usr/lib/gimp/2.0/plug-ins")

    pisitools.dodoc("README.txt")
