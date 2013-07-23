#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

import os

WorkDir = "Jalbum"

def fixperms(d):
    for root, dirs, files in os.walk(d):
        for name in dirs:
            shelltools.chmod(os.path.join(root, name), 0755)
        for name in files:
            shelltools.chmod(os.path.join(root, name), 0644)

def install():
    fixperms(".")

    pisitools.insinto("/opt/jalbum","*")

    pisitools.removeDir("/opt/jalbum/lib/sunos")
    pisitools.removeDir("/opt/jalbum/lib/windows")
    pisitools.remove("/opt/jalbum/StartJAlbum.bat")
    pisitools.remove("/opt/jalbum/plugins/*.bat")
    pisitools.remove("/opt/jalbum/plugins/*.java")
