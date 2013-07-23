#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "w3c-libwww-5.4.0"

def setup():
    shelltools.export("WANT_AUTOCONF", "2.50")
    shelltools.export("WANT_AUTOMAKE", "1.9")

    autotools.autoreconf("-fi")

    autotools.configure("ac_cv_lib_rx_regexec=no \
                         --without-mysql \
                         --enable-shared \
                         --disable-static \
                         --with-dav \
                         --with-md5 \
                         --with-zlib \
                         --with-expat \
                         --with-ssl \
                         --with-gnu-ld \
                         --with-regex")

def build():
    autotools.make("check-am")
    autotools.make()

def install():
    autotools.rawInstall('DESTDIR="%s"' % get.installDIR())

    pisitools.dodoc("ChangeLog")
    pisitools.dohtml(".")
