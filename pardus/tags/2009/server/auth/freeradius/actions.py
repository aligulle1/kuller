#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get
import os

WorkDir = "freeradius-server-%s" % get.srcVERSION()

def setup():
    shelltools.export("CFLAGS", "%s -DLDAP_DEPRECATED -fPIC -DPIC" % get.CFLAGS())
    shelltools.export("LDFLAGS", "%s -pie" % get.LDFLAGS())

    autotools.configure("--prefix=/usr \
                         --exec-prefix=/usr \
                         --sysconfdir=/etc \
                         --localstatedir=/var \
                         --datadir=/usr/share \
                         --sharedstatedir=/var \
                         --oldincludedir=/usr/include \
                         --includedir=/usr/include \
                         --mandir=/usr/share/man \
                         --with-rlm-sql_postgresql-include-dir=/usr/include/postgresql \
                         --with-rlm-krb5-include-dir=/usr/include/kerberosIV \
                         --with-rlm-sql_mysql-include-dir=/usr/include/mysql \
                         --without-rlm_dbm \
                         --without-rlm_eap_tnc \
                         --without-rlm_eap_ikev2 \
                         --without-rlm_opendirectory \
                         --without-rlm_sql_oracle \
                         --without-rlm_sql_iodbc \
                         --without-rlm_sql_db2 \
                         --without-rlm_sql_firebird \
                         --with-openssl-includes=/usr/include/openssl \
                         --with-gnu-ld \
                         --with-experimental-modules \
                         --disable-ltdl-install \
                         --enable-strict-dependencies \
                         --with-edir \
                         --with-system-libtool \
                         --with-udp-fromto \
                         --disable-static \
                         --with-pic")

def build():
    autotools.make("-j1")

def install():
    autotools.rawInstall("R=%s" % get.installDIR())

    pisitools.insinto("/usr/share/doc/freeradius/", "suse")
    pisitools.insinto("/usr/share/doc/freeradius/", "debian")
    pisitools.insinto("/usr/share/doc/freeradius/", "redhat")
    pisitools.insinto("/usr/share/doc/freeradius/", "scripts")

    pisitools.dosed("%s/etc/raddb/radiusd.conf"%get.installDIR(), '^#user *= *radius', 'user = radiusd')
    pisitools.dosed("%s/etc/raddb/radiusd.conf"%get.installDIR(), '^#group *= *radius', 'group = radiusd')

    pisitools.dodoc("CREDITS", "README", "COPYRIGHT", "LICENSE", "todo/TODO")

