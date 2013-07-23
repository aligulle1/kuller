#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009-2011 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import get

shelltools.export("HOME", get.workDIR())

def setup():
    #autotools.autoreconf("-vfi")
    shelltools.system("./autogen.sh --prefix=/usr \
                        --sysconfdir=/etc \
                        --localstatedir=/var \
                        --disable-static \
                        --disable-dependency-tracking \
                        --enable-more-warnings=no \
                        --enable-introspection \
                        --with-crypto=nss \
                        --with-distro=pardus \
                        --with-resolvconf=/etc/resolv.conf \
                        --with-system-ca-path=/etc/ssl/certs \
                        --with-tests")

def build():
    autotools.make()

def check():
    autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.insinto("/usr/share/dbus-1/interfaces/", "introspection/*.xml")

    pisitools.dodir("/etc/NetworkManager/VPN")

    pisitools.dodoc("README", "COPYING")
