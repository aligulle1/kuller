#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

WorkDir = "cfitsio"

def setup():
    autotools.rawConfigure("--prefix=/usr \
                            --libdir=/usr/lib \
                            --includedir=/usr/include")

def build():
    autotools.make("shared")

def install():
    autotools.install()

    pisitools.dodoc("*.txt", "README")
