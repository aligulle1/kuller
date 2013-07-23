#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "squid-%s" % get.srcVERSION().replace("0.", "0.STABLE")

def setup():
    #autotools.autoreconf()

    shelltools.export("CFLAGS","%s -fpie" % get.CFLAGS())
    shelltools.export("CXXFLAGS","%s -fpie" % get.CXXFLAGS())
    shelltools.export("LDFLAGS","%s -pie" % get.LDFLAGS())

    autotools.configure("--sysconfdir=/etc/squid \
                         --localstatedir=/var \
                         --libexecdir=/usr/lib/squid \
                         --datadir=/usr/share/squid \
                         --enable-auth=\"basic,digest,ntlm\" \
                         --enable-removal-policies=\"lru,heap\" \
                         --enable-digest-auth-helpers=\"password\" \
                         --enable-basic-auth-helpers=\"LDAP,PAM,SASL,getpwnam,NCSA,SMB,MSNT,multi-domain-NTLM\" \
                         --enable-external-acl-helpers=\"ldap_group,ip_user,session,unix_group,wbinfo_group\" \
                         --enable-ntlm-auth-helpers=\"SMB,fakeauth\" \
                         --enable-negotiate-auth-helpers=\"squid_kerb_auth\" \
                         --enable-ident-lookups \
                         --enable-useragent-log \
                         --enable-cache-digests \
                         --enable-delay-pools \
                         --enable-referer-log \
                         --enable-arp-acl \
                         --with-pthreads \
                         --with-large-files \
                         --enable-htcp \
                         --enable-carp \
                         --enable-follow-x-forwarded-for \
                         --enable-snmp \
                         --enable-ssl \
                         --enable-linux-netfilter \
                         --enable-storeio=ufs,diskd,aufs,null \
                         --enable-async-io \
                         --enable-icap-client \
                         --with-default-user=squid \
                         --host=%s" % get.HOST())

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodir("/var/cache/squid")
    pisitools.dodir("/var/log/squid")

    pisitools.dosym("/usr/share/squid/errors/English", "/etc/squid/errors")

    pisitools.doman("helpers/basic_auth/LDAP/*.8")
    pisitools.dohtml("helpers/basic_auth/MSNT/README.html", "RELEASENOTES.html")
    pisitools.dodoc("helpers/basic_auth/SASL/squid_sasl_auth*")
    pisitools.dodoc("CONTRIBUTORS", "CREDITS", "ChangeLog", "QUICKSTART", "doc/*.txt", "helpers/ntlm_auth/no_check/README.no_check_ntlm_auth")
