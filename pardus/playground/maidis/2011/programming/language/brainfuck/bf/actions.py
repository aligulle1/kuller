#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools

WorkDir = "."

def build():
    shelltools.system("nasm -f bin -o bf bf.asm.txt")

def install():
    pisitools.dobin("bf")

    pisitools.dodoc("bf.asm.txt")
