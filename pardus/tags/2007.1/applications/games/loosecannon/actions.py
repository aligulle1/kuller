#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get

import os

def setup():
    for root, dirs, files in os.walk("share"):
        for name in dirs:
            shelltools.chmod(os.path.join(root, name), 0755)
        for name in files:
            shelltools.chmod(os.path.join(root, name), 0644)

    autotools.configure("--enable-simd \
                         --enable-binreloc \
                         --enable-binreloc-threads")

def build():
    autotools.make()

def install():
    pisitools.dobin("src/loosecannon")
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "README")
    pisitools.dodir("/usr/share")
    shelltools.copytree("share/loosecannon", "%s/usr/share/" % get.installDIR())

    pythonmodules.fixCompiledPy()
