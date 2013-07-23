#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="iTest-%s-src" % get.srcVERSION()
BuildDir="%s/%s" % (get.workDIR(),WorkDir)

def setup():
    for directory in [".", "iTestClient", "iTestServer"]:
        shelltools.cd("%s/%s" % (BuildDir, directory))
        shelltools.system("qmake-qt4")

    for directory in ["iTestClient", "iTestServer"]:
        shelltools.cd("%s/%s/i18n" % (BuildDir, directory))
        shelltools.system("lrelease-qt4 *.ts")

def build():
    autotools.make()

def install():
    pisitools.dobin("bin/iTestClient")
    pisitools.dobin("bin/iTestServer")

    for pixmap in ["itest.png", "itestwri.png"]:
        pisitools.insinto("/usr/share/pixmaps", pixmap)

    pisitools.dodoc("readme.txt")
