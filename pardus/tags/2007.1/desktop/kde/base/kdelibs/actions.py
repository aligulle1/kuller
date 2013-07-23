#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005,2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import kde
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    autotools.make("-f admin/Makefile.common")
    kde.configure("--with-distribution=\"Pardus 2007\" \
                   --disable-libfam \
                   --enable-inotify \
                   --with-libart \
                   --with-libidn \
                   --with-utempter \
                   --with-alsa \
                   --with-arts \
                   --with-ssl \
                   --with-tiff \
                   --with-gssapi \
                   --with-openexr \
                   --with-jasper \
                   --enable-cups \
                   --enable-dnssd \
                   --with-aspell \
                   --with-acl \
                   --without-lua \
                   --without-hspell")

def build():
    kde.make()

    shelltools.export("LC_ALL","C") # Workaround a doxygen bug until we fix it
    kde.make("apidox")

def install():
    kde.install()
    kde.install("install-apidox")

