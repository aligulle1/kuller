#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006,2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("doc/mkcert.sh", "dovecot-openssl.cnf", "/etc/dovecot/ssl/openssl.cnf")
    autotools.configure("--sysconfdir=/etc/dovecot \
                         --localstatedir=/var \
                         --enable-ipv6 \
                         --with-ioloop=best \
                         --with-poll=best \
                         --with-storages=\"maildir,mbox\" \
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

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.insinto("/etc/dovecot/ssl", "doc/mkcert.sh")

    pisitools.dodoc("AUTHORS", "NEWS", "README", "TODO")
    pisitools.dodoc("doc/*.txt", "doc/*.conf", "doc/*.cnf")

    pisitools.dodir("/etc/dovecot/ssl")
    pisitools.dodir("/var/run/dovecot")
    pisitools.dodir("/var/run/dovecot/login")

    pisitools.removeDir("/usr/share/doc/dovecot")
    pisitools.remove("/etc/dovecot/dovecot-example.conf")
