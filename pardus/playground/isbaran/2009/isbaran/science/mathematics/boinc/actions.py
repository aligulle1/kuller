#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get


def setup():
    shelltools.export("CFLAGS", "-O3 -funroll-loops -fforce-addr -ffast-math %s" % get.CFLAGS())
    shelltools.export("CXXFLAGS", "-O3 -funroll-loops -fforce-addr -ffast-math %s" % get.CXXFLAGS())

    pisitools.dosed("configure.ac", "BOINC_SET_COMPILE_FLAGS", "")

    shelltools.system("aclocal -I m4")
    shelltools.system("autoheader")
    shelltools.system("automake")
    shelltools.system("autoconf")

    autotools.configure("--prefix=/usr \
                         --exec-prefix=/usr \
                         --localstatedir=/var \
                         --sbindir=/usr/sbin \
                         --with-ssl \
                         --disable-server \
                         --disable-static-client \
                         --enable-dynamic-client-linkage \
                         --disable-fcgi \
                         --enable-client \
                         --enable-generic-processor \
                         --disable-static \
                         --enable-shared \
                         --enable-unicode \
                         --disable-dependency-tracking \
                         --with-ssl \
                         --with-wx-config=wx-config")

def build():
    pisitools.dosed("*/Makefile", "LDFLAGS =", "LDFLAGS = -L../lib")

    autotools.make("-j1")

def install():
    autotools.rawInstall('DESTDIR=%s' % get.installDIR())

    #pisitools.removeDir("/etc/init.d")
    pisitools.removeDir("/etc/sysconfig")

    pisitools.dodoc("COPYING", "COPYRIGHT", "notes")
