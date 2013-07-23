#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

import os

WorkDir = "magicor-1.0-rc1"
sharedir = "/usr/share/magicor"
NoStrip = "/"

def fixperms(d):
    for root, dirs, files in os.walk(d):
        for name in dirs:
            shelltools.chmod(os.path.join(root, name), 0755)
        for name in files:
            shelltools.chmod(os.path.join(root, name), 0644)
            if name.endswith(".pyc"):
                shelltools.unlink(os.path.join(root, name))

def setup():
    fixperms("data")

def install():
    pisitools.dodir("/usr/share")
    shelltools.copytree("data", "%s/%s" % (get.installDIR(), sharedir))

