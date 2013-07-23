#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

import os

WorkDir = "l1-linux-v%s/src" % get.srcVERSION()

def fixperms(d):
    for root, dirs, files in os.walk(d):
        for name in dirs:
            shelltools.chmod(os.path.join(root, name), 0755)
        for name in files:
            shelltools.chmod(os.path.join(root, name), 0644)

def setup():
    fixperms("./")
    pisitools.dosed("Makefile", "SUBDIRS=", "M=")
    pisitools.dosed("Makefile", "BUILD_KERNEL=.*", "BUILD_KERNEL = %s" % get.curKERNEL())
    pisitools.dosed("Makefile", "shell uname -r", "shell echo %s" % get.curKERNEL())

def build():
    autotools.make("BUILD_KERNEL=/lib/modules/%s/build default" % get.curKERNEL())

def install():
    pisitools.insinto("/lib/modules/%s/extra" % get.curKERNEL(), "*.ko")

    shelltools.cd("..")
    pisitools.dodoc("copying", "readme", "release_note.txt")
    pisitools.doman("atl1.7")

