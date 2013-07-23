#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

import os

WorkDir = "openarena-%s" % get.srcVERSION()
NoStrip = "/"

docs = ["CHANGES", "COPYING", "CREDITS", "LINUXNOTES", "README", "*.txt"]
datadir = "/usr/share/openarena/baseoa"

def fixperms(d):
    for root, dirs, files in os.walk(d):
        for name in dirs:
            shelltools.chmod(os.path.join(root, name), 0755)
        for name in files:
            shelltools.chmod(os.path.join(root, name), 0644)

def setup():
    fixperms("baseoa")
    for f in docs:
        shelltools.chmod(f, 0644)

def install():
    pisitools.insinto(datadir, "baseoa/*")

    for f in docs:
        pisitools.dodoc(f)
