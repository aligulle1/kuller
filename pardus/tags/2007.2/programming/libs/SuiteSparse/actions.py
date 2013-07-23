#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def build():
    shelltools.makedirs("dist")

    shelltools.export("SYSTEM_CFLAGS","%s -O3" % get.CFLAGS())
    autotools.make()

def install():
    pisitools.dodir("/usr/include/ufsparse")

    shelltools.copy("UFconfig/UFconfig.h", "%s/usr/include/ufsparse/UFconfig.h" % get.installDIR())
    shelltools.copy("AMD/Include/amd.h", "%s/usr/include/ufsparse/amd.h" % get.installDIR())
    shelltools.copy("BTF/Include/btf.h", "%s/usr/include/ufsparse/btf.h" % get.installDIR())
    shelltools.copy("CHOLMOD/Include/*.h", "%s/usr/include/ufsparse" % get.installDIR())
    shelltools.copy("COLAMD/colamd.h", "%s/usr/include/ufsparse/colamd.h" % get.installDIR())
    shelltools.copy("CCOLAMD/ccolamd.h", "%s/usr/include/ufsparse/ccolamd.h" % get.installDIR())
    shelltools.copy("KLU/Include/klu.h", "%s/usr/include/ufsparse/klu.h" % get.installDIR())
    shelltools.copy("UMFPACK/Include/*.h", "%s/usr/include/ufsparse" % get.installDIR())
    shelltools.copy("CAMD/Include/*.h", "%s/usr/include/ufsparse" % get.installDIR())
    shelltools.copy("CXSparse/Source/cs.h", "%s/usr/include/ufsparse" % get.installDIR())

    for header in shelltools.ls("%s/usr/include/ufsparse/*.h" % get.installDIR()):
        shelltools.chmod("/usr/include/ufsparse/%s" % header, 0644)

    shelltools.move("dist","%s/usr/lib" % get.installDIR())
