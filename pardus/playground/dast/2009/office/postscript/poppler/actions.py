#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.makedirs("build")
    shelltools.cd("build")
    cmaketools.configure("--DENABLE-STATIC=OFF \
                         --DENABLE-A4-PAPER=ON \
                         --DENABLE-XPDF-HEADERS=ON \
                         --DBUILD_GTK_TESTS=OFF \
                         --DBUILD_QT3_TESTS=OFF \
                         --DBUILD_QT4_TESTS-OFF \
                         --DENABLE-SPLASH=OFF \
                         --DENABLE-ZLIB=ON", sourceDir="..")

def build():
    shelltools.cd("build")
    cmaketools.make()

def install():
    shelltools.cd("build")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
    shelltools.cd("..")
    pisitools.dodoc("README", "AUTHORS", "ChangeLog", "NEWS", "README-XPDF", "TODO")
    pisitools.doman("utils/*.1")
