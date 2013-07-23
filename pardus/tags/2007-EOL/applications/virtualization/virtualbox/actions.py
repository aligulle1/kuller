#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007,2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

#WorkDir="VirtualBox-%s_OSE" % get.srcVERSION()
WorkDir="VirtualBox-1.5.6_OSE"

def setup():
    autotools.rawConfigure("--disable-pulse")

def build():
    shelltools.system("source env.sh && kmk")
    shelltools.cd("out/linux.x86/release/bin/src")
    autotools.make()

def install():
    for file in ["VirtualBox","VBoxSVC","VBoxXPCOMIPCD","VBoxBFE","VBoxManage","VBoxSDL","VBoxTunctl","vditool",
                 "*.so","*.xpt","*.r0","*.gc","components","nls"]:
        pisitools.insinto("/usr/share/VirtualBox","out/linux.x86/release/bin/%s" % file)

    # Kernel module
    pisitools.insinto("/lib/modules/%s/extra" % get.curKERNEL(), "out/linux.x86/release/bin/src/vboxdrv.ko")

    # Symlinks
    pisitools.dosym("/usr/bin/VBox.sh","/usr/bin/VirtualBox")
    pisitools.dosym("/usr/bin/VBox.sh","/usr/bin/VBoxManage")
    pisitools.dosym("/usr/bin/VBox.sh","/usr/bin/VBoxSDL")

    # Remove tests
    pisitools.remove("/usr/share/VirtualBox/tst*")
