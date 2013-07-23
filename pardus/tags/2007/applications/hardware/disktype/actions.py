#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005,2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    autotools.make('CC="%s" CFLAGS="%s"' % ( get.CC(), get.CFLAGS()))

def install():
    pisitools.dobin ("disktype")
    pisitools.dodoc("README", "HISTORY", "TODO")
