#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    cmaketools.configure()

    shelltools.system("lrelease-qt4 QDevelop.pro")

def build():
    cmaketools.make()

def install():
    pisitools.dobin("qdevelop")
    pisitools.insinto("/usr/share/pixmaps", "resources/images/logo.png", "qdevelop.png")

    pisitools.dodoc("ChangeLog.txt", "README.txt", "copying")
