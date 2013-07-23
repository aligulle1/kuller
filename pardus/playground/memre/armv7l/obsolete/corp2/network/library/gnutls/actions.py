#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import crosstools as autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools

def setup():
    shelltools.export("AUTOPOINT", "true")
    pisitools.dosed("Makefile.am", r"(^SUBDIRS\s*=.*)doc\s*tests", "\\1")
    autotools.autoreconf("-fi")
    autotools.configure("--disable-static \
                         --disable-rpath \
                         --disable-dependency-tracking \
                         --enable-guile \
                         --with-lzo \
                         --with-zlib \
                         --with-included-libcfg \
                         --without-libgcrypt-prefix")

def build():
    autotools.make()

def check():
    autotools.make("check")

def install():
    autotools.install()

