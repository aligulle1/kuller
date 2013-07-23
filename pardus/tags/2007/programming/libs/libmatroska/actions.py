#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005, 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("make/linux/Makefile", "CXXFLAGS=", "CXXFLAGS+=")

def build():
    shelltools.cd("make/linux")

    # workaround for gcc 3.4
    shelltools.export("CXXFLAGS", "%s -finput-charset=ISO8859-15" % get.CXXFLAGS())
    
    autotools.make("PREFIX=/usr \
                   LIBEBML_INCLUDE_DIR=/usr/include/ebml \
                   LIBEBML_LIB_DIR=/usr/lib")

def install():
    shelltools.cd("make/linux")

    autotools.install("libdir=%s/usr/lib" % get.installDIR())
    pisitools.dodoc("../../ChangeLog")
