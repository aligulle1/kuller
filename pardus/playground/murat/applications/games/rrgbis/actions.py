#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
import os

WorkDir = "rrgbis"
datadir = "/usr/share/rrgbis"
NoStrip = [datadir]

def fixperms(d):
    for root, dirs, files in os.walk(d):
        for name in dirs:
            shelltools.chmod(os.path.join(root, name), 0755)
        for name in files:
            shelltools.chmod(os.path.join(root, name), 0644)

def setup():
    fixperms(get.workDIR())

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.insinto(datadir, "settings.dat")
    pisitools.insinto("/usr/share/pixmaps", "rrgbis.png")

    for data in ("aiscripts", "images", "missions", "music", "sound", "squirrelscripts", "unitdata", "unitpictures"):
        pisitools.insinto(datadir, data)

    pisitools.dodoc("*.txt")
