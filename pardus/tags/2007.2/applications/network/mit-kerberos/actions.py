#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir="krb5-%s/src" % get.srcVERSION()

def setup():
    shelltools.export("DB_HEADER","/usr/include/db_185.h")
    shelltools.export("DB_LIB","/usr/lib/libdb.so")

    autotools.configure("--with-system-db \
                         --with-krb4 \
                         --without-tcl \
                         --enable-ipv6 \
                         --enable-shared \
                         --localstatedir=/etc \
                         --with-system-et \
                         --with-system-ss \
                         --enable-dns-for-realm")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # Add "k" prefix to some apps and manpages to resolve conflicts
    for app in ["telnetd","ftpd"]:
        pisitools.rename("/usr/share/man/man8/%s.8" % app, "k%s.8" % app)
        pisitools.rename("/usr/sbin/%s" % app, "k%s" % app)

    for app in ["rcp","rsh","telnet","ftp","rlogin"]:
        pisitools.rename("/usr/share/man/man1/%s.1" % app, "k%s.1" % app)
        pisitools.rename("/usr/bin/%s" % app, "k%s" % app)

    # TODO comar service for kadmind and krb5kdc
    pisitools.removeDir("/etc/init.d")
