#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--with-kernel-headers=/usr/include \
                         --sysconfdir=/etc/racoon \
                         --enable-dependency-tracking \
                         --disable-security-context \
                         --disable-static \
                         --enable-shared \
                         --enable-rc5 \
                         --enable-idea \
                         --enable-adminport \
                         --enable-frag \
                         --enable-gssapi \
                         --enable-stats \
                         --enable-dpd \
                         --enable-natt \
                         --enable-fastquit \
                         --enable-stats \
                         --enable-ipv6")

def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.dodoc("ChangeLog", "README")

