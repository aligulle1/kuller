#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.configure()
    ''' info ve man dizinlerini düzelt '''
    pisitools.dosed("Makefile", "/info", "/share/info")
    pisitools.dosed("Makefile", "/man/", "/share/man/") 

def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.dodoc("ChangeLog", "README", "TODO", "doc/barcode.pdf", "doc/barcode.ps")
