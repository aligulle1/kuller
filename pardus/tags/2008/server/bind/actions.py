#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="bind-9.4.1-P1"

def setup():
    for e in ("bin/named/named.8", "bin/check/named-checkconf.8", "bin/rndc/rndc.8"):
        pisitools.dosed(e, "/etc/named.conf", "/etc/bind/named.conf")
        pisitools.dosed(e, "/etc/rndc.conf", "/etc/bind/rndc.conf")
        pisitools.dosed(e, "/etc/rndc.key", "/etc/bind/rndc.key")

    autotools.autoconf()

    autotools.configure("--localstatedir=/var \
                         --with-libtool \
                         --sysconfdir=/etc/bind \
                         --enable-linux-caps \
                         --enable-threads \
                         --enable-ipv6 \
                         --with-randomdev=/dev/urandom \
                         --with-pic \
                         --enable-libbind \
                         --with-openssl=/usr \
                         --disable-static")

def build():
    shelltools.export("MAKEOPTS","-j1")
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("CHANGES", "COPYRIGHT", "FAQ", "README")
    pisitools.dodoc("doc/misc/*", "doc/draft/*", "doc/rfc/*", "contrib/named-bootconf/named-bootconf.sh", "contrib/nanny/nanny.pl")
    pisitools.dohtml("doc/arm/*")

    pisitools.dodir("/var/bind")
    pisitools.dodir("/var/bind/pri")
    pisitools.dodir("/var/bind/sec")
    pisitools.dodir("/var/run/named")

    pisitools.dosym("/var/bind/pri","/etc/bind/pri")
    pisitools.dosym("/var/bind/sec","/etc/bind/sec")
    pisitools.dosym("/var/bind/named.ca","/var/bind/root.cache")
    pisitools.remove("/usr/bin/isc-config.sh")
