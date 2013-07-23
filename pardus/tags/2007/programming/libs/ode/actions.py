#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005, 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get


def setup():
#    autotools.autoreconf()
    autotools.configure("--enable-release \
                         --disable-double-precision \
                         --enable-opcode \
                         --enable-gyroscopic")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("CHANGELOG.txt", "README.txt")
    pisitools.dohtml("docs/*")
