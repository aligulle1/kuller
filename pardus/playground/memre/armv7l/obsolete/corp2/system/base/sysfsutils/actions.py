#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import crosstools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    crosstools.configure("--libdir=/lib \
                          --disable-static")

def build():
    crosstools.make()

def install():
    crosstools.rawInstall("DESTDIR=%s" % (get.installDIR()))

    # We do not distribute this
    pisitools.remove("/usr/bin/dlist_test")

    pisitools.dodoc("docs/libsysfs.txt")
    pisitools.dodoc("AUTHORS", "COPYING", "ChangeLog", "NEWS", "README", "TODO")

