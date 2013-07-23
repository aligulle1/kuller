#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import crosstools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.export("PYTHON_PREFIX", "%(SysRoot)s/usr" % crosstools.environment)
    crosstools.environment["CFLAGS"] = "%(CFLAGS)s -DNDEBUG" % crosstools.environment

    crosstools.autoreconf("-vif")
    crosstools.configure("--disable-static \
                          --disable-xevie \
                          --disable-xprint \
                          --without-doxygen")

def build():
    crosstools.make()

def install():
    crosstools.install()

    pisitools.dodoc("COPYING", "NEWS", "README")
