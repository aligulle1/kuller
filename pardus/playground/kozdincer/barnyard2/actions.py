#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2011 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools

def setup():
    autotools.autoreconf("-vfi -I ./m4")
    autotools.configure("--disable-static \
                         --enable-ipv6 \
                         --enable-gre \
                         --enable-mpls \
                         --disable-64bit-gcc \
                         --disable-prelude \
                         --disable-debug \
                         --disable-mysql-ssl-support \
                         --disable-aruba \
                         --disable-broi \
                         --with-odbc \
                         --with-mysql \
                         --with-postgresql \
                         --without-oracle \
                         --without-broccoli")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.insinto("/usr/share/barnyard2", "schemas/create_db2")
    pisitools.insinto("/usr/share/barnyard2", "schemas/create_mysql")
    pisitools.insinto("/usr/share/barnyard2", "schemas/create_postgresql")

    pisitools.dodir("/var/log/barnyard2")

    pisitools.dodoc("COPYING", "LICENSE", "README", "RELEASE.NOTES", "doc/README.database")
