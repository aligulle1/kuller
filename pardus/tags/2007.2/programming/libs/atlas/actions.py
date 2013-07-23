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

import os
import os.path

WorkDir="ATLAS"

def build():
    makefile = get.workDIR()+"/ATLAS/Make.Linux_PIIISSE2"
    pisitools.dosed(makefile,"REPLACE_WITH_TOPDIR","%s" % get.workDIR())

    for root,dirs,files in os.walk(os.getcwd()):
        for file in files:
            if file == "Make.inc":
                symlink = os.path.join(root,file)
                shelltools.unlink(symlink)
                shelltools.sym(makefile,symlink)
            
    # build netlib-lapack
    shelltools.cd("netlib-lapack/SRC")
    shelltools.system("FC=\"g77\" make static")
    
def install():
    autotools.rawInstall("arch=Linux_PIIISSE2 install")

    pisitools.dodir("/usr/lib")
    pisitools.dodir("/usr/include")
    
    # Merge netlib-lapack with atlas-lapack library
    shelltools.system("mkdir tmp")
    shelltools.cd("tmp")
    shelltools.system("ar x ../lib/Linux_*/liblapack.a")
    shelltools.system("ar r ../netlib-lapack/SRC/liblapack.a *.o")
    shelltools.cd("..")
    
    pisitools.dolib("lib/Linux_*/*.a")
    pisitools.dolib("netlib-lapack/SRC/liblapack.a")
    shelltools.copy("include/cblas.h","%s/usr/include/cblas.h" % get.installDIR())
    shelltools.copy("include/clapack.h","%s/usr/include/clapack.h" % get.installDIR())    

    pisitools.dodoc("README","doc/*.ps","doc/.txt")
    
