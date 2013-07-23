#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007,2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "db-%s" % get.srcVERSION()

def setup():
    shelltools.cd("build_unix")

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
                       --host=%s \
                       --enable-java \
                       --disable-cxx \
                       --disable-tcl \
                       --disable-static \
                       --build=%s" % (get.HOST(), get.HOST()))

def build():
    shelltools.cd("build_unix")
    autotools.make()

def install():
    shelltools.cd("build_unix")

    pisitools.dolib(".libs/libdb_java*.so")
    pisitools.insinto("/usr/share/java","db.jar")
