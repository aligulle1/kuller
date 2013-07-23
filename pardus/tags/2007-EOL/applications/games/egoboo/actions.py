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

WorkDir = "egoboo"
data = "/usr/share/egoboo"

def fixperms(d):
    for root, dirs, files in os.walk(d):
        for name in dirs:
            shelltools.chmod(os.path.join(root, name), 0755)
        for name in files:
            shelltools.chmod(os.path.join(root, name), 0644)

def build():
    shelltools.cd("code")
    autotools.make("clean")
    autotools.make('FLAGS="-D_LINUX %s" CC="%s" egoboo' % (get.CFLAGS(), get.CC()))

def install():
    pisitools.dodoc("egoboo.txt")
    pisitools.dodir(data)

    for d in ["basicdat", "import", "modules", "players", "text",]:
        fixperms(d)
        shelltools.copytree(d, "%s/%s" % (get.installDIR(), data))

    shelltools.chmod("code/egoboo", 0755)
    shelltools.copy("code/egoboo", "%s/%s" % (get.installDIR(), data))

