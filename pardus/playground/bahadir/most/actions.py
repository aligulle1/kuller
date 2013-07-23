#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.configure("--without-x")

def build():
    autotools.make()

def install():
    pisitools.dobin("src/objs/most")
    pisitools.doman("most.1")
    pisitools.dodoc("README", "most.rc", "lesskeys.rc", "most-fun.txt")

