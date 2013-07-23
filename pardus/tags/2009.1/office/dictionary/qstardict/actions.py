#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import get

shelltools.export("HOME", get.workDIR())

def setup():
    shelltools.system("qmake-qt4")

    shelltools.cd("qstardict/translations")
    shelltools.system("lrelease-qt4 *.ts")

    shelltools.cd("../../kdeplasma")
    cmaketools.configure("-DCMAKE_INSTALL_PREFIX=/usr/kde/4", sourceDir=".")

def build():
    autotools.make("CXX=%s" % get.CXX())

    shelltools.cd("kdeplasma")
    cmaketools.make()

def install():
    shelltools.cd("kdeplasma")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
    shelltools.cd("..")

    autotools.install("INSTALL_ROOT=%s" % get.installDIR())

    pisitools.insinto("/usr/share/pixmaps", "qstardict/pixmaps/qstardict.png")

    pisitools.removeDir("/usr/share/doc/qstardict")

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "README", "THANKS")
