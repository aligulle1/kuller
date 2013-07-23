#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

import os

NoStrip = "/"

datadir = "/usr/share/WesternQuake3/basewq3"

def fixperms(d):
    for root, dirs, files in os.walk(d):
        for name in dirs:
            shelltools.chmod(os.path.join(root, name), 0755)
        for name in files:
            shelltools.chmod(os.path.join(root, name), 0644)

def install():
    for files in ["*.pk3", "*.cfg"]:
        fixperms(files)
        pisitools.insinto(datadir, files)

    pisitools.dodoc("*.txt")
    pisitools.dohtml("manual/*")
