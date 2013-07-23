#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

import os
from os.path import join


def setup():
    pisitools.dosed("share/config.h", 'CONFIG_DATA "./data"', 'CONFIG_DATA "/usr/share/neverball/data"')
    pisitools.dosed("Makefile", "-O3", get.CFLAGS())
    pisitools.dosed("Makefile", "^MAPC_TARG= mapc", "MAPC_TARG= neverball-mapc")

    # Permissions, permissions, permissions
    for root, dirs, files in os.walk("data"):
        for name in dirs:
            shelltools.chmod(join(root, name), 0755)
        for name in files:
            shelltools.chmod(join(root, name), 0644)

def build():
    autotools.make()

def install():
    pisitools.dobin("neverball")
    pisitools.dobin("neverball-mapc")
    pisitools.dobin("neverputt")

    pisitools.dodir("/usr/share/neverball")
    shelltools.copytree("data", "%s/usr/share/neverball/data" % get.installDIR())
    pisitools.dodoc("CHANGES", "README")
    shelltools.chmod("icon/*.png", 0644)
    pisitools.insinto("/usr/share/pixmaps", "icon/*.png")
