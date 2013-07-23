#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import crosstools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "db-%s/build_unix" % get.srcVERSION()

def setup():
    crosstools.environment["LDFLAGS"] = "%(LDFLAGS)s -Wl,--default-symver" % crosstools.environment
    shelltools.system("../dist/configure \
                       --build=%(build)s --host=%(host)s \
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
                       --disable-test" % crosstools.environment)

def build():
    crosstools.make()

def install():
    crosstools.install('libdir="%s/usr/lib"' % get.installDIR())

    # Move docs
    pisitools.domove("/usr/docs/", "/usr/share/doc/%s/html/" % get.srcNAME())
