#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--prefix=/usr \
                         --exec-prefix=/usr \
                         --enable-gui=no \
                         --includedir=/usr/include/iODBC \
                         --libdir=/usr/lib/iODBC \
                         --with-iodbc-inidir=/etc/iODBC \
                         --disable-gtktest \
                         --disable-static \
                         --sysconfdir=/etc/iODBC \
                         --datadir=/usr/share/iODBC \
                         --with-iodbc-filedsnpath=/etc/iODBC")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.remove("/usr/lib/iODBC/*.a")

    #Move .pc file(s) to /usr/lib/pkgconfig
    pisitools.domove("/usr/lib/iODBC/pkgconfig/*", "/usr/lib/pkgconfig/")
    pisitools.removeDir("/usr/lib/iODBC/pkgconfig")

    pisitools.dodoc("AUTHORS", "ChangeLog", "NEWS", "README")
