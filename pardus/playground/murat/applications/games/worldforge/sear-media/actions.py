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
datadir = "/usr/share/sear"

def fixperms(d):
    for root, dirs, files in os.walk(d):
        for name in dirs:
            shelltools.chmod(os.path.join(root, name), 0755)
        for name in files:
            shelltools.chmod(os.path.join(root, name), 0644)

def install():
    pisitools.dodir(datadir)
    for data in os.listdir("."):
        fixperms(data)

        if os.path.isfile(data):
            pisitools.insinto(datadir, data)

        if os.path.isdir(data):
            shelltools.copytree(data, "%s%s" % (get.installDIR(), datadir))

    pisitools.dodoc("*.txt")
