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
    autotools.configure("--with-xml2 \
                         --with-ssl \
                         --with-zlib \
                         --without-gssapi \
                         --with-ssl=openssl \
                         --enable-threadsafe-ssl=posix \
                         --enable-shared \
                         --disable-static")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dosed("%s/usr/bin/neon-config" % get.installDIR(),"-Wl,-Bdirect -Wl,-hashvals -Wl,-zdynsort","")

    pisitools.dodoc("THANKS", "TODO", "ChangeLog", "AUTHORS", "BUGS", "NEWS", "README", "doc/*")
