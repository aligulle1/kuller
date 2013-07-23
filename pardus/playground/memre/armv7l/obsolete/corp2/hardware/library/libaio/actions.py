#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import crosstools as autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    autotools.make()

def install():
    autotools.rawInstall("destdir=%s prefix=/ libdir=/lib \
                          includedir=/usr/include usrlibdir=/usr/lib" % get.installDIR())

    pisitools.remove("/usr/lib/libaio.a")

    pisitools.remove("/lib/libaio.so.1")
    pisitools.remove("/usr/lib/libaio.so")

    pisitools.dosym("libaio.so.1.0.1", "/lib/libaio.so.1")
    pisitools.dosym("../../lib/libaio.so.1.0.1", "/usr/lib/libaio.so")


    pisitools.dodoc("ChangeLog", "COPYING", "TODO")
