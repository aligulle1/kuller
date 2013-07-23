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
    pisitools.dosed("pydevice.h", "device.h", "parted.h")
    pisitools.dosed("pyfilesystem.h", "disk.h", "parted.h")
    pisitools.dosed("pygeometry.h", "geomk.h", "parted.h")
    
    autotools.configure("--with-python-version=2.4")
    
def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.dodoc("AUTHORS", "COPYING", "README", "ChangeLog")
