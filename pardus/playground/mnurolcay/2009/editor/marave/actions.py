#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import get
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools

def build():
    pythonmodules.compile()

def install():
    pythonmodules.install()

    #shelltools.chmod("build.in/fedora/taskcoach.desktop", 0644)
    #pisitools.insinto("/usr/share/applications", "build.in/fedora/taskcoach.desktop")
    #pisitools.insinto("/usr/share/pixmaps", "icons.in/taskcoach.png")

    #pisitools.dosym("/usr/bin/taskcoach.py", "/usr/bin/taskcoach")

    pisitools.dodoc("LICENSE", "README")
