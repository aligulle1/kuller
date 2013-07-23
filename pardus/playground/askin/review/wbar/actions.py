#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def build():
    autotools.make()

def install():
    pisitools.dobin("wbar", "/usr/bin")
    pisitools.insinto("/usr/share/wbar", "iconpack")
    pisitools.dosym("/usr/share/wbar/iconpack/comic.ttf", "/usr/share/wbar/iconpack/wbar.osx/font.ttf")
    pisitools.insinto("/usr/share/wbar", "dot.wbar")
