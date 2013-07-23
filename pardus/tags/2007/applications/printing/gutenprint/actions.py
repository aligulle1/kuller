#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

WorkDir="gutenprint-5.0.0"

def setup():
    autotools.configure("--with-cups \
                         --with-foomatic3 \
                         --with-ghostscript \
                         --disable-test \
                         --disable-testpattern \
                         --disable-libgutenprintui \
                         --disable-libgutenprintui2 \
                         --without-gimp \
                         --without-gimp2 \
                         --enable-static-genppd \
                         --disable-static \
                         --disable-nls")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s install" % get.installDIR())

    pisitools.dohtml("%s/usr/share/gutenprint/doc/reference-html/*" % get.installDIR())
    pisitools.removeDir("/usr/share/gutenprint/doc/")
