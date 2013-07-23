#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get


def setup():
    shelltools.export("CFLAGS", "-O3 -funroll-loops -fforce-addr -ffast-math %s" % get.CFLAGS())
    shelltools.export("CXXFLAGS", "-O3 -funroll-loops -fforce-addr -ffast-math %s" % get.CXXFLAGS())

    autotools.autoreconf("-vif")

    autotools.configure("--prefix=/usr \
                         --exec-prefix=/usr \
                         --localstatedir=/var \
                         --sbindir=/usr/sbin \
                         --enable-client \
                         --enable-dynamic-client-linkage \
                         --disable-server \
                         --with-ssl \
                         --disable-static \
                         --enable-unicode \
                         --with-wx-config=/usr/bin/wx-config")

def build():
    pisitools.dosed("*/Makefile", "LDFLAGS =", "LDFLAGS = -L../lib")

    autotools.make("-j1")

def install():
    autotools.rawInstall('DESTDIR=%s' % get.installDIR())

    pisitools.dodoc("COPYING", "COPYRIGHT", "notes")
