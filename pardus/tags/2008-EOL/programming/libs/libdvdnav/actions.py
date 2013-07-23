#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "libdvdnav-4.1.1_p997"

def setup():
    shelltools.system('./configure2 \
                       --prefix=/usr \
                       --libdir=/usr/lib \
                       --shlibdir=/usr/lib \
                       --disable-static \
                       --enable-shared \
                       --with-dvdread=/usr/include/dvdread \
                       --disable-strip \
                       --disable-opts \
                       --extra-cflags="%s" \
                       --disable-debug' % get.CFLAGS())

def build():
    autotools.make("version.h")
    autotools.make("-j1")

def install():
    #fix dvdnav-config
    pisitools.dosed("Makefile", "'prefix='\\$\\(PREFIX\\)", "'prefix='/usr")
    pisitools.dosed("Makefile", "'libdir='\\$\\(shlibdir\\)", "'libdir='/usr/lib")

    autotools.rawInstall('DESTDIR="%s"' % get.installDIR())

    pisitools.dodoc("AUTHORS", "DEVELOPMENT-POLICY.txt", "ChangeLog", "TODO", "doc/dvd_structures")
