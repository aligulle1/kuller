#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "gpicd-%s-1" %get.srcVERSION()

def build():
    autotools.make()

def install():
    pisitools.dobin("rpm/INSTALL/usr/bin/*")

    # install lib_a
    pisitools.dolib_a("lib/gpicd.a")

    # install samples
    pisitools.insinto("usr/share/gpicd/sample", "sample/*")
    pisitools.remove("/usr/share/gpicd/sample/Makefile")

    # Icon file
    pisitools.insinto("/usr/share/pixmaps", "gui/chip.xpm", "gpicd.xpm")

    # Documets
    pisitools.dohtml("doc/*")
    pisitools.dodoc("ChangeLog", "README")
