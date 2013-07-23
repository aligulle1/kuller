#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "songbird"

def build():
    autotools.make("-f songbird.mk")

def install():
    shelltools.makedirs("%s/usr/share/" % get.installDIR())
    shelltools.copytree("compiled/dist", "%s/usr/share/songbird" % get.installDIR())

    pisitools.insinto("/usr/share/pixmaps/", "app/branding/icon64.png", "songbird.png")
    pisitools.dosym("/usr/share/songbird/songbird-bin", "/usr/bin/songbird")
