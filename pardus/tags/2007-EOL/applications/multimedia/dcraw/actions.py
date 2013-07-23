#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def build():
    shelltools.system("gcc -o dcraw -O4 dcraw.c -lm -ljpeg -llcms")
    
def install():
    pisitools.dobin("dcraw")
