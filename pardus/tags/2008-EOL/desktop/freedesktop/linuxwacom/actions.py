#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "linuxwacom-%s" % get.srcVERSION().replace("_", "-")

def setup():
    shelltools.export("CFLAGS", "%s -I/usr/include/dbus-1.0 -I/usr/lib/dbus-1.0/include" % get.CFLAGS())

    autotools.autoreconf("-vif")
    autotools.configure("--disable-static \
                         --enable-dlloader \
                         --without-gtk \
                         --without-tk \
                         --without-tcl")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "README*", "NEWS")
