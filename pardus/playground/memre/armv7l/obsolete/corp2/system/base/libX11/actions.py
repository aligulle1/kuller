#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import crosstools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    crosstools.autoreconf("-vif")

    crosstools.configure("--disable-static \
                          --disable-specs \
                          --with-xcb \
                          --enable-malloc0returnsnull")

def build():
    crosstools.make('-C src/util \
                     CC="%(HOSTCC)s" \
                     CC_FOR_BUILD="%(CC)s" \
                     CFLAGS= ' % crosstools.environment)

    crosstools.make()

def install():
    crosstools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README")
