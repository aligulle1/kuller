#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2005,2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import libtools
from pisi.actionsapi import get

WorkDir = "db-4.2.52"

def setup():
    shelltools.cd("build_unix")

    libtools.gnuconfig_update()

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
