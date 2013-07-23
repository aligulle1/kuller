#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "flock/mozilla"

shelltools.export("MOZ_BUILD_DATE", "2007070900")
shelltools.export("BUILD_OFFICIAL", "1")
shelltools.export("MOZILLA_OFFICIAL", "1")

def setup():
    autotools.autoconf()
    autotools.configure('--enable-optimize="%s -Os"' % get.CXXFLAGS())

def build():
    autotools.make("-j1")

def install():
    pisitools.insinto("/usr/lib/", "dist/bin", "flock", sym=False)

    # Install docs
    pisitools.dodoc("LEGAL", "LICENSE")
