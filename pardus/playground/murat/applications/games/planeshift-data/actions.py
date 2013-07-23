#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

import os

NoStrip = "/"

data = ["art", "data", "docs", "guide", "support"]
datadir = "/usr/share/planeshift"

def fixperms(d):
    for root, dirs, files in os.walk(d):
        for name in dirs:
            shelltools.chmod(os.path.join(root, name), 0755)
        for name in files:
            shelltools.chmod(os.path.join(root, name), 0644)

def setup():
    # gui/ directory in the planeshift package is more recent
    shelltools.unlinkDir("data/gui")

def install():
    for f in ("*.cfg", "*.xml"):
        pisitools.insinto(datadir, f)

    for f in data:
        fixperms(f)
        shelltools.copy(f, "%s/%s" % (get.installDIR(), datadir))
