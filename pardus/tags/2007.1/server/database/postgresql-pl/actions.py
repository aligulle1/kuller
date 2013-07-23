#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2007  TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "postgresql-8.1.8"

def setup():
    autotools.configure("--with-python \
                         --with-perl \
                         --include=/usr/include/postgresql \
                         --with-tcl \
                         --with-krb5 \
                         --with-openssl \
                         --enable-nls \
                         --with-pam \
                         --enable-integer-datetimes \
                         --enable-thread-safety \
                         --enable-thread-safety-force \
                         --enable-depend \
                         --host=%s \
                         --libdir=/usr/lib \
                         --disable-rpath \
                         --with-docdir=/usr/share/doc/postgresql \
                        " % get.CHOST())

def build():
    if get.LDFLAGS():
        ld = "LD=%s %s" % (get.LD(), get.LDFLAGS())
    else:
        ld = "LD=%s" % get.LD()

    autotools.make(ld)

    shelltools.cd("contrib")
    autotools.make(ld)
    shelltools.cd("..")

    shelltools.cd("contrib/xml2")
    autotools.make(ld)
    shelltools.cd("../..")

def install():
    autotools.rawInstall("DESTDIR=%s LIBDIR=%s/usr/lib" % (get.installDIR(), get.installDIR()))

    shelltools.cd("contrib")
    autotools.rawInstall("DESTDIR=%s LIBDIR=%s/usr/lib" % (get.installDIR(), get.installDIR()))
    shelltools.cd("..")

    shelltools.cd("contrib/xml2")
    autotools.rawInstall("DESTDIR=%s LIBDIR=%s/usr/lib" % (get.installDIR(), get.installDIR()))
    shelltools.cd("../..")

    pisitools.dodoc("README", "HISTORY", "COPYRIGHT", "INSTALL")
    pisitools.dodoc("contrib/adddepend/*")
    pisitools.dodoc("doc/FAQ*", "doc/README.*", "doc/TODO", "doc/bug.template")

    pisitools.dodir("/var/lib/postgresql")
    pisitools.dodir("/var/lib/postgresql/data")
    pisitools.dodir("/var/lib/postgresql/backups")
