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

def setup():
    shelltools.export("CC","/usr/bin/mpicc")

    autotools.configure("--disable-static \
                         --enable-linux-lfs \
                         --with-ssl \
                         --enable-parallel")
    
def build():
    autotools.make()
    
def install():
    install_dir = get.installDIR()
    autotools.make("prefix=%s/usr docdir=%s/usr/share/doc/hdf5-%s-%s libdir=%s/usr/lib/ install"
                    % (install_dir,install_dir,get.srcVERSION(),get.srcRELEASE(),install_dir))
    
    pisitools.dodoc("README.txt","COPYING","MANIFEST")
    pisitools.dohtml("doc/html/*")

    # This is needed for testing only
    pisitools.remove("/usr/bin/h5perf")
