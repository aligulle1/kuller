#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005, 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.echo("include/ldap_defaults.h", "#define LDAPI_SOCK \"/var/run/openldap/slapd.sock\"")
    autotools.configure("--prefix=/usr \
                         --enable-bdb \
                         --with-ldbm-api=berkeley \
                         --enable-hdb=mod \
                         --enable-slapd \
                         --enable-slurpd \
                         --enable-ldbm \
                         --enable-passwd=mod \
                         --enable-phonetic=mod \
                         --enable-dnssrv=mod \
                         --enable-ldap \
                         --enable-wrappers \
                         --enable-meta=mod \
                         --enable-monitor=mod \
                         --enable-null=mod \
                         --enable-shell=mod \
                         --enable-rewrite \
                         --enable-rlookups \
                         --enable-aci \
                         --enable-modules \
                         --enable-cleartext \
                         --enable-lmpasswd \
                         --enable-spasswd \
                         --enable-slapi \
                         --enable-dyngroup \
                         --enable-proxycache \
                         --enable-perl \
                         --enable-syslog \
                         --enable-dynamic \
                         --enable-local \
                         --enable-proctitle \
                         --enable-overlay \
                         --with-tls \
                         --with-cyrus-sasl \
                         --enable-crypt \
                         --enable-ipv6")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("ANNOUNCEMENT", "CHANGES", "COPYRIGHT", "README", "LICENSE")
    pisitools.dodir("/var/run/openldap")
    pisitools.dodir("/var/run/openldap/slapd")
    pisitools.dodir("/etc/openldap/ssl")
