#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="VirtualBox-OSE-%s" % get.srcVERSION()

def setup():
    autotools.rawConfigure()

def build():
    shelltools.system("source env.sh && kmk")
    shelltools.cd("out/linux.x86/release/bin/src")
    autotools.make()

def install():
    for file in ["VirtualBox","VBoxSVC","VBoxXPCOMIPCD","VBoxBFE","VBoxManage","VBoxSDL","vditool","*.so","*.xpt","*.r0","*.gc","components"]:
        pisitools.insinto("/usr/share/VirtualBox","out/linux.x86/release/bin/%s" % file)

    pisitools.insinto("/lib/modules/%s/extra" % get.curKERNEL(), "out/linux.x86/release/bin/src/vboxdrv.ko")

    # Symlinks
    pisitools.dosym("/usr/bin/VBox.sh","/usr/bin/VirtualBox")
    pisitools.dosym("/usr/bin/VBox.sh","/usr/bin/VBoxManage")
    pisitools.dosym("/usr/bin/VBox.sh","/usr/bin/VBoxSDL")

    # Remove tests
    pisitools.remove("/usr/share/VirtualBox/tst*")
