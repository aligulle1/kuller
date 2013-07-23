#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "db-%s/build_unix" % get.srcVERSION()

def setup():
    shelltools.export("LDFLAGS","%s -Wl,--default-symver" % get.LDFLAGS())
    shelltools.system("../dist/configure \
                       --prefix=/usr \
                       --mandir=/usr/share/man \
                       --infodir=/usr/share/info \
                       --datadir=/usr/share \
                       --sysconfdir=/etc \
                       --localstatedir=/var/lib \
                       --libdir=/usr/lib \
                       --enable-compat185 \
                       --with-uniquename \
                       --enable-rpc \
                       --enable-cxx \
                       --disable-tcl \
                       --disable-java \
                       --disable-static \
                       --disable-test")

def build():
    autotools.make()

def install():
    autotools.install('libdir="%s/usr/lib"' % get.installDIR())

    # Remove unnecessary binaries
    pisitools.removeDir("/usr/bin")

    # Remove links
    pisitools.remove("/usr/lib/libdb_cxx-4.so")
    pisitools.remove("/usr/lib/libdb_cxx.so")
    pisitools.remove("/usr/lib/libdb-4.so")
    pisitools.remove("/usr/lib/libdb.so")

    # Move headers under /usr/include/db-4.5
    shelltools.makedirs("%s/usr/include/db-4.5" % get.installDIR())
    pisitools.domove("/usr/include/*.h", "/usr/include/db-4.5")

    # Move docs
    pisitools.domove("/usr/docs/", "/usr/share/doc/%s/html/" % get.srcNAME())
