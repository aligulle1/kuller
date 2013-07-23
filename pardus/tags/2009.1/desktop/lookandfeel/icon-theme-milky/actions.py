#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

import os

WorkDir = "./"
NoStrip = ["/"]

icondir = "/usr/share/icons"
iconsrc = "milky"

def fixperms(d, workaround=False):
    for root, dirs, files in os.walk(d):
        for name in dirs:
            shelltools.chmod(os.path.join(root, name), 0755)
        for name in files:
            shelltools.chmod(os.path.join(root, name), 0644)

def setup():
    fixperms(iconsrc, workaround=True)

def install():
    pisitools.insinto(icondir, iconsrc)


