#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

import os

NoStrip = "/"

datadir = "/usr/share/urbanterror/baseut4"

def fixperms(d):
    for root, dirs, files in os.walk(d):
        for name in dirs:
            shelltools.chmod(os.path.join(root, name), 0755)
        for name in files:
            shelltools.chmod(os.path.join(root, name), 0644)

def install():
    for files in ["zpak000.pk3", "*.cfg", "mapcycle.txt"]:
        pisitools.insinto(datadir, files)

    for dirs in ["demos", "screenshots"]:
        shelltools.copytree(dirs, "%s/%s" % (get.installDIR(), datadir))

    pisitools.rename("%s/demos/test.dm_68" % datadir, "TEST.dm_68")

    pisitools.dodoc("*.txt")

    fixperms(get.installDIR())
