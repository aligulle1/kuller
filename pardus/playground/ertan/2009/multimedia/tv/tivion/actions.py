#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools

def install():
    pisitools.dobin("src/tivion")

    pisitools.insinto("/usr/share/tivion", "src/*.py")
    pisitools.insinto("/usr/share/tivion", "src/data")
    pisitools.insinto("/usr/share/locale", "src/lang/*")

    pisitools.insinto("/usr/share/applications", "src/tivion.desktop")
    pisitools.insinto("/usr/share/pixmaps", "src/data/img/tivion-launcher.png", "tivion.png")

    pisitools.dodoc("AUTHORS", "README", "LICENSE")
