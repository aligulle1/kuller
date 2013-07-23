#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import qt4

def setup():
    qt4.configure("Tamanoir.pro")

def build():
    qt4.make()

def install():
    qt4.install()

    pisitools.dobin("tamanoir")

    pisitools.insinto("/usr/share/applications", "debian/tamanoir.desktop")
    pisitools.insinto("/usr/share/pixmaps", "icon/tamanoir.png")

    pisitools.dodoc("gpl-3.0.txt", "docs/*.txt")
