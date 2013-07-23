#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools

def build():
    shelltools.system("g++ yilbasi.cpp -o yilbasi")

def install():
    pisitools.dobin("yilbasi")

    pisitools.dodoc("yilbasi.cpp")
