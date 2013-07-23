#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules

WorkDir="aggdraw-1.2a3-20060212"

def install():
    pythonmodules.install()
    
    pisitools.dodoc("CHANGES","README")
