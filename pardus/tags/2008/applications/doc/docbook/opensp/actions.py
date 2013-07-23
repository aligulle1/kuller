#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get

WorkDir = "OpenSP-%s" % get.srcVERSION()

def setup():
    autotools.configure("--enable-nls \
                         --enable-http \
                         --disable-doc-build \
                         --enable-default-catalog=/etc/sgml/catalog \
                         --enable-default-search-path=/usr/share/sgml \
                         --datadir=/usr/share/sgml/opensp")

def build():
    autotools.make("pkgdocdir=/usr/share/doc/%s" % get.srcTAG())

def install():
    autotools.rawInstall('DESTDIR="%s" pkgdocdir=/usr/share/doc/%s' % (get.installDIR(), get.srcTAG()))
