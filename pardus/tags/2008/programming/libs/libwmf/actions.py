#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools

def setup():
    autotools.configure("--with-expat \
                         --without-libxml2 \
                         --with-jpeg \
                         --with-x \
                         --with-gsfontdir=/usr/share/ghostscript/fonts \
                         --with-fontdir=/usr/share/libwmf/fonts \
                         --with-docdir=/usr/share/doc/%s \
                         --disable-static" % get.srcTAG() )
def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s \
                          fontdir=/usr/share/libwmf/fonts \
                          wmfonedocdir=/usr/share/doc/%s/caolan \
                          wmfdocdir=/usr/share/doc/%s" %
                          ( get.installDIR(), get.srcTAG(), get.srcTAG() ) )

    pisitools.dodoc("README", "AUTHORS", "CREDITS", "ChangeLog", "NEWS", "TODO")

