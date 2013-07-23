#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

WorkDir = "zsnes_1_42/src"

def setup():
    autotools.autoreconf()
    autotools.configure()

def build():
    autotools.make()

def install():
    pisitools.dobin("zsnes")
    pisitools.dodoc("../docs/*.txt", "../docs/README.LINUX")
    pisitools.insinto("/usr/share/pixmaps", "icons/48x48x32.png", "zsnes.png")
