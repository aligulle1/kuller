#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import crosstools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    crosstools.configure("--disable-static \
                          --with-libssl-prefix=%(RootDir)s/usr/lib \
                          --with-libgcrypt-prefix=%(RootDir)s/usr/lib" % \
                          crosstools.environment)

def build():
    crosstools.make()

def install():
    crosstools.install()

    pisitools.dodoc("README", "AUTHORS", "COPYING", "ChangeLog")
