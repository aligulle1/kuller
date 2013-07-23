#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

def setup():
    autotools.configure("--with-cups \
                         --with-foomatic3 \
                         --with-ghostscript \
                         --with-escputil \
                         --with-readline \
                         --disable-test \
                         --disable-testpattern \
                         --disable-libgutenprintui \
                         --disable-libgutenprintui2 \
                         --without-gimp \
                         --without-gimp2 \
                         --enable-static-genppd \
                         --enable-epson \
                         --disable-static \
                         --disable-nls")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s install" % get.installDIR())

    pisitools.dohtml("%s/usr/share/gutenprint/doc/reference-html/*" % get.installDIR())
    pisitools.removeDir("/usr/share/gutenprint/doc/")
