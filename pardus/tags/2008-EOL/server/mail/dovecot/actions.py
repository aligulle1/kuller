#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import libtools
from pisi.actionsapi import get

def setup():
    autotools.autoreconf()
    autotools.automake()
    libtools.libtoolize('--copy --force')
    pisitools.dosed("doc/mkcert.sh", "dovecot-openssl.cnf", "/etc/dovecot/ssl/openssl.cnf")
    shelltools.export("CFLAGS","%s  -D_REENTRANT -D_GNU_SOURCE  -ldb-4.6" % get.CFLAGS())
    shelltools.export("CPPFLAGS","%s  -ldb-4.6" % get.CXXFLAGS())
    shelltools.export("LDFLAGS","%s -Wl,--as-needed" % get.LDFLAGS())
    autotools.configure("--sysconfdir=/etc/dovecot \
                         --localstatedir=/var \
                         --enable-ipv6 \
                         --with-ioloop=best \
                         --with-poll=best \
                         --with-db \
                         --with-mysql \
                         --with-pgsql \
                         --with-pop3d \
                         --with-ssl=openssl \
                         --with-ssldir=/etc/ssl \
                         --with-pam \
                         --with-gssapi \
                         --with-ldap \
                         --disable-static")

def build():
    autotools.make()

    shelltools.cd("sieve")
    autotools.configure("--with-dovecot=../")
    autotools.make()

    shelltools.cd("../managesieve")
    autotools.configure("--with-dovecot=../ --with-dovecot-sieve=../sieve")
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    shelltools.cd("sieve")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    shelltools.cd("../managesieve")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    shelltools.cd("../")
    
    pisitools.insinto("/etc/dovecot/ssl", "doc/mkcert.sh")

    pisitools.dodir("/etc/dovecot/ssl")
    pisitools.dodir("/var/run/dovecot")
    pisitools.dodir("/var/run/dovecot/login")

    pisitools.removeDir("/usr/share/doc/dovecot")
    pisitools.remove("/etc/dovecot/dovecot-example.conf")

    pisitools.dodoc("AUTHORS", "NEWS", "README", "TODO")
    pisitools.dodoc("doc/*.txt", "doc/*.conf", "doc/*.cnf")