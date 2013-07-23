#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.export("DSOFLAGS", get.LDFLAGS())
    autotools.configure("--with-cups-user=pnp \
                         --with-cups-group=pnp \
                         --with-system-groups=pnpadmin \
                         --with-docdir=/usr/share/cups/html \
                         --localstatedir=/var \
                         --enable-pam \
                         --enable-ssl \
                         --enable-gnutls \
                         --enable-slp \
                         --enable-nls \
                         --enable-dbus \
                         --enable-png \
                         --enable-jpeg \
                         --enable-tiff \
                         --enable-pie \
                         --without-rcdir \
                         --enable-threads \
                         --enable-ldap \
                         --enable-libpaper \
                         --without-php")

def build():
    autotools.make()

def install():
    autotools.rawInstall("BUILDROOT=%s" % get.installDIR())

    pisitools.dodir("/usr/share/cups/profiles")
    pisitools.dodir("/usr/libexec/cups/driver")
    pisitools.dodir("/var/log/cups")
    pisitools.dodir("/var/run/cups/certs")
    pisitools.dodir("/var/cache/cups")
    pisitools.dodir("/var/spool/cups/tmp")

    pisitools.dodoc("CHANGES.txt", "CREDITS.txt", "ENCRYPTION.txt", "LICENSE.txt", "README.txt")

    pisitools.dosym("/usr/share/cups/docs", "/usr/share/doc/%s/html" % get.srcTAG())

    # cleanups
    pisitools.removeDir("/etc/pam.d")
    pisitools.removeDir("/usr/share/applications")

    # allow raw printing
    pisitools.dosed("%s/etc/cups/mime.types" % get.installDIR(), "^#application/octet-stream", "application/octet-stream")

    # Enable network connections use PCL drivers, for other OS clients (yes, raw printing)
    pisitools.dosed("%s/etc/cups/mime.convs" % get.installDIR(), "^#application/octet-stream", "application/octet-stream")

    # Let cups use all available protocols, like slp
    pisitools.dosed("%s/etc/cups/cupsd.conf" % get.installDIR(), "^#BrowseProtocols.*", "BrowseProtocols all")

