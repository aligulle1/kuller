#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir="FTGL/unix"

def setup():
    autotools.configure("--enable-shared \
                         --disable-static")
def build():
    autotools.make()

    shelltools.cd("docs")
    autotools.make()

def install():
    autotools.install()

    shelltools.cd("..")
    pisitools.dodoc("HISTORY.txt", "README.txt", "COPYING.txt")

