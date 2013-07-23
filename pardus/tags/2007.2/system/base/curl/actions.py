#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2005,2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--enable-static=no \
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
                         --enable-largefile")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("CHANGES", "README", "docs/FEATURES", "docs/INSTALL", \
                    "docs/INTERNALS", "docs/LIBCURL", "docs/MANUAL", "docs/FAQ", \
                    "docs/BUGS", "docs/CONTRIBUTE")

    # Remove Bdirect from pkgconfig file
    pisitools.dosed("%s/usr/lib/pkgconfig/libcurl.pc" % get.installDIR(),"-Wl,-Bdirect -Wl,-hashvals -Wl,-zdynsort","")
