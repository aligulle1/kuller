#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2011 TUBITAK/BILGEM
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def build():
    shelltools.cd("src")
    autotools.make('CC=%s CFLAGS="%s"' % (get.CC(), get.CFLAGS()))

def install():
    shelltools.cd("src")

    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.remove("/etc/init.d")

    shelltools.cd("..")
    pisitools.dodoc("LICENSE")

