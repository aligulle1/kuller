#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--with-libexif")

def build():
    autotools.make()
    
def install():
    pisitools.dosed("Makefile", "/usr/lib/gimp/", "%s/usr/lib/gimp/" % get.installDIR())
    autotools.install()
