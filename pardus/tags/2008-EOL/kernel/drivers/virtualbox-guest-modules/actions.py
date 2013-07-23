#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "."

def build():
    modules = ("vboxadd", "vboxvfs")
    for module in modules:
        if module != "vboxadd":
            shelltools.copy("vboxadd/Module.symvers", module)
        autotools.make("-C %s KERN_DIR=/lib/modules/%s/build" % (module, get.curKERNEL()))

def install():
    pisitools.insinto("/lib/modules/%s/extra" % get.curKERNEL(), "*/*.ko")
