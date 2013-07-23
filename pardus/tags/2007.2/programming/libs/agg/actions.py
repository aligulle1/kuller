#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005,2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    shelltools.chmod("autogen.sh",0755)
    shelltools.system("./autogen.sh --prefix=/usr \
                       --disable-examples \
                       --enable-ctrl \
                       --enable-platform \
                       --enable-freetype \
                       --enable-gpc \
                       --enable-static=no")
def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("ChangeLog", "README.txt")
