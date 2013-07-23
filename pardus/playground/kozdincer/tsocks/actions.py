#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2011 TUBITAK/BILGEM
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "tsocks-1.8"

def setup():
    autotools.configure("--libdir=/usr/lib \
                         --with-conf=/etc/tsocks/tsocks.conf \
                         --enable-socksdns \
                         --disable-hostnames")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" %(get.installDIR()))

    pisitools.insinto("/etc/tsocks", "tsocks.conf.simple.example", "tsocks.conf")
    pisitools.insinto("/etc/tsocks", "tsocks.conf.complex.example")

    pisitools.dobin("inspectsocks")
    pisitools.dobin("saveme")
    pisitools.dobin("validateconf")

    pisitools.dodoc("ChangeLog", "COPYING", "FAQ", "TODO")
