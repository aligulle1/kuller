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

site_conf = """
CC = %s
LFLAGS = %s
LIBDIR = /usr/lib
INCDIR = /usr/include
ETC = /etc/dhcp
VARDB = /var/lib/dhcp
VARRUN = /var/run/dhcp
ADMMANDIR = /usr/share/man/man8
ADMMANEXT = .8
FFMANDIR = /usr/share/man/man5
FFMANEXT = .5
LIBMANDIR = /usr/share/man/man3
LIBMANEXT = .3
USRMANDIR = /usr/share/man/man1
USRMANEXT = .1
MANCAT = man
"""

def setup():
    pisitools.dosed("client/scripts/linux", "/etc/dhclient-exit-hooks", "/etc/dhcp/dhclient-exit-hooks")
    pisitools.dosed("client/scripts/linux", "/etc/dhclient-enter-hooks", "/etc/dhcp/dhclient-enter-hooks")

    shelltools.echo("site.conf", site_conf % (get.CC(), get.LDFLAGS()))
    autotools.rawConfigure("--copts -DPARANOIA")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodir("/etc/dhcp")
    pisitools.dodir("/var/run/dhcp")
    shelltools.touch("%s/var/lib/dhcp/dhcpd.leases" % get.installDIR())
    pisitools.dodoc("README", "RELNOTES", "doc/*")
