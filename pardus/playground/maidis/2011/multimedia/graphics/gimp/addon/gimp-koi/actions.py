#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools

def build():
    shelltools.system("gimptool-2.0 --build Koi.c")

def install():
    pisitools.dobin("Koi", "/usr/lib/gimp/2.0/plug-ins")

    pisitools.dodoc("README")
