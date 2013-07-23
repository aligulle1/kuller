#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.rawConfigure("--enable-bindir=/usr/sbin \
                            --enable-sysconfdir=/etc/sarg \
                            --enable-htmldir=/var/www/localhost/htdocs \
                            --enable-mandir=/usr/share/man/man1")

def build():
    autotools.make()

def install():
    pisitools.dodir("/var/www/localhost/htdocs/squid-reports")
    pisitools.dodir("/etc/sarg")
    pisitools.dosbin("sarg")
    pisitools.insinto("/etc/sarg", "images")
    pisitools.insinto("/etc/sarg","languages")
    pisitools.insinto("/etc/sarg","fonts")
    pisitools.doman("sarg.1")
    pisitools.dodoc("BETA-TESTERS", "CONTRIBUTORS", "README", "ChangeLog", "htaccess")
