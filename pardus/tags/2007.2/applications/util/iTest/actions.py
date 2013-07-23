#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="iTest-%s-src" % get.srcVERSION()
BuildDir="%s/%s" % (get.workDIR(),WorkDir)

def setup():
    for directory in [".","database_editor","test_writer"]:
        shelltools.cd("%s/%s" % (BuildDir,directory))
        shelltools.system("qmake-qt4")

    for directory in ["database_editor","test_writer"]:
        shelltools.cd("%s/%s/i18n" % (BuildDir,directory))
        shelltools.system("lrelease-qt4 *.ts")

def build():
    autotools.make()

def install():
    pisitools.dobin("iTest")
    pisitools.dobin("iTestWri")

    for pixmap in ["itest.png","itestwri.png"]:
        pisitools.insinto("/usr/share/pixmaps",pixmap)
        shelltools.chmod("%s/usr/share/pixmaps/%s" % (get.installDIR(),pixmap), 0644)

    pisitools.dodoc("readme.txt")
