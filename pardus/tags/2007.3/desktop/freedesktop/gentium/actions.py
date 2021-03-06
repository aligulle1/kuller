#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir="Gentium102"

def install():
    shelltools.chmod("*.TTF",0644)
    pisitools.insinto("/usr/share/fonts/gentium/","*.TTF")

    pisitools.dodoc("GENTIUM-FAQ.txt","OFL-FAQ.txt","OFL.txt","QUOTES.txt","README.txt")
    
