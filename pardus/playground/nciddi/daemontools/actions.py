#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "admin/daemontools-%s" % get.srcVERSION()

def setup():
    shelltools.touch("src/home")

def build():
    shelltools.cd("src")
    shelltools.system("make")

def install():
    shelltools.cd("src")
    for i in open("../package/commands", "r").readlines():
        pisitools.dobin(i.strip("\n"))
    pisitools.dodoc("CHANGES", "../package/README", "TODO")
