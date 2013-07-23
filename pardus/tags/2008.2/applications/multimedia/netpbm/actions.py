#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    autotools.make('CFLAGS="%s -fPIC" LDFLAGS="%s" -j1' % (get.CFLAGS(), get.LDFLAGS()))

def install():
    pisitools.dodir("/")
    autotools.make('package pkgdir=%s/usr' % get.installDIR())

    pisitools.dosym("/usr/lib/libnetpbm.so.10","/usr/lib/libnetpbm.so")

    pisitools.remove("/usr/include/shhopt.h")
    pisitools.remove("/usr/bin/doc.url")
    pisitools.remove("/usr/bin/manweb")

    for data in ["VERSION","pkginfo","README","config_template"]:
        pisitools.remove("/usr/%s" % data)

    for directory in ["link","man/web"]:
        pisitools.removeDir("/usr/%s" % directory)

    pisitools.domove("/usr/misc", "/usr/share/netpbm")
    pisitools.domove("/usr/man", "/usr/share")

    pisitools.dodoc("README", "doc/*LICENSE*")
