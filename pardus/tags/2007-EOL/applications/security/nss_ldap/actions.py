#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.autoreconf()
    autotools.configure("--with-ldap-lib=openldap \
                         --with-ldap-conf-file=/etc/security/ldap.conf \
                         --with-ldap-secret-file=/etc/security/ldap.secret \
                         --enable-rfc2307bis \
                         --enable-paged-results"
    )

def build():
    autotools.make()

def install():
    pisitools.dodir("/etc")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("ChangeLog", "ANNOUNCE", "NEWS", "README", "AUTHORS", "ldap.conf")
