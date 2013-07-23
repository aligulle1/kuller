#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import crosstools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    crosstools.autoreconf("-fiv")
    crosstools.configure("--disable-static \
                          --with-gnu-ld \
                          --disable-man-pages \
                          --disable-gtk-doc-html")

def build():
    crosstools.make("-j1")

def install():
    crosstools.install()

    pisitools.dodoc("COPYING", "AUTHORS")
