#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

import os

WorkDir = "Impact"

def fixperms(d):
    for root, dirs, files in os.walk(d):
        for name in dirs:
            shelltools.chmod(os.path.join(root, name), 0755)
        for name in files:
            shelltools.chmod(os.path.join(root, name), 0644)

def install():
    shelltools.export("JAVA_HOME", "/opt/sun-jdk")
    fixperms(".")
    shelltools.system("ant")
    shelltools.chmod("impact.png", 0644)
    pisitools.insinto("/usr/share/pixmaps", "impact.png")
    pisitools.insinto("/opt/Impact", "*")

    pisitools.dodoc("doc/*", "examples/*")
