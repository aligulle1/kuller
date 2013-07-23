#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.export("CFLAGS","%s -fPIC" % get.CFLAGS())
    shelltools.export("F9X","gfortran")

    autotools.configure("--enable-cxx \
                         --enable-fortran \
                         --enable-threadsafe \
                         --with-pthread \
                         --with-ssl")

def build():
    autotools.make()

def check():
    autotools.make("check")

def install():
    autotools.install("docdir=%s/usr/share/doc/%s" % (get.installDIR(),get.srcTAG()))

    # Unneeded stuff
    pisitools.remove("/usr/bin/h5perf")
    pisitools.remove("/usr/lib/*.a")

    pisitools.dohtml("doc/html/*")
    pisitools.dodoc("README.txt","COPYING")
