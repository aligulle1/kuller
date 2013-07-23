#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import crosstools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    crosstools.configure("--disable-static \
                          --enable-ipv6 \
                          --disable-ldap \
                          --with-ssl \
                          --enable-http \
                          --enable-ftp \
                          --enable-gopher \
                          --enable-file \
                          --enable-dict \
                          --enable-manual \
                          --enable-telnet \
                          --enable-nonblocking \
                          --enable-largefile \
                          --with-ca-bundle=/etc/ssl/certs/ca-bundle.crt \
                          --with-random=/dev/random")

def build():
    crosstools.make()

def install():
    crosstools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("CHANGES", "docs/FEATURES", "docs/MANUAL", "docs/FAQ", "docs/BUGS")
