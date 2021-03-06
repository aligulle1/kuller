#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    shelltools.export("CFLAGS", '%s -fpie -DSYSLOGD_PIDNAME=\\\"syslogd.pid\\\"' % get.CFLAGS())
    shelltools.export("LDFLAGS", "-pie -Wl,-z,relro -Wl,-z,now")

    autotools.configure("--disable-static \
                         --enable-mysql \
                         --enable-pgsql \
                         --enable-gnutls \
                         --enable-gssapi-krb5 \
                         --disable-relp \
                         --disable-testbench \
                         --sbindir=/sbin \
                         --enable-mail \
                         --enable-imfile \
                         --enable-unlimited-select")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.insinto("%s/%s" % (get.docDIR(), get.srcNAME()),
                      "plugins/ommysql/createDB.sql",
                      "createMySQLDB.sql")

    pisitools.insinto("%s/%s" % (get.docDIR(), get.srcNAME()),
                      "plugins/ompgsql/createDB.sql",
                      "createPgSQLDB.sql")

    pisitools.dodoc("COPYING*", "README", "AUTHORS", "ChangeLog")
