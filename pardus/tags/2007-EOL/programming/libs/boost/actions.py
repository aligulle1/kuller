#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2005,2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

WorkDir="boost_1_33_1"

def build():
    # Build boost-jam
    pisitools.cd("./tools/build/jam_src/")
    shelltools.system("./build.sh")

def install():
    shelltools.system("./tools/build/jam_src/bin.linuxx86/bjam -sPYTHON_ROOT=/usr -sPYTHON_VERSION=2.4 -sTOOLS=gcc -sBUILD=release --prefix=%s/usr install" % get.installDIR())

    # Remove duplicate/unneeded libraries
    pisitools.remove("/usr/lib/*.a")
    pisitools.remove("/usr/lib/*.so")
    pisitools.remove("/usr/lib/*gcc-mt-d*")
    pisitools.remove("/usr/lib/*gcc.so")
    pisitools.remove("/usr/lib/*gcc-d*")

    # Create symlinks
    libraries = shelltools.ls("%s/usr/lib" % get.installDIR())
    for lib in libraries:
        fixedName = lib.replace("-gcc-mt-1_33_1.so.1.33.1","")
        fixedName = fixedName.replace("-gcc-1_33_1.so.1.33.1","")
        pisitools.dosym("%s" % lib, "/usr/lib/%s.so" % fixedName)
       
    shelltools.move("%s/usr/include/boost-1_33_1/boost" % get.installDIR() ,"%s/usr/include/boost" % get.installDIR())
    pisitools.removeDir("/usr/include/boost-1_33_1")

    pisitools.dodoc("ChangeLog", "AUTHORS", "INSTALL*", "NEWS", "README*")
    
