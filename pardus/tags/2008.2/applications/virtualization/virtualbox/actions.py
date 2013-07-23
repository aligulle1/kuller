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

WorkDir="VirtualBox-%s" % get.srcVERSION()

def setup():
    autotools.rawConfigure("--disable-hardening\
                            --disable-qt3\
                            --with-qt4-dir=/usr/qt/4")

def build():
    shelltools.system("source env.sh && kmk all")
    shelltools.cd("out/linux.x86/release/bin/src")
    autotools.make("KERN_DIR=/usr/src/linux-%s" % get.curKERNEL())

def install():
    for file in ["VirtualBox","VBoxSVC","VBoxXPCOMIPCD","VBoxBFE","VBoxManage","VBoxSDL",\
                 "VBoxTunctl","VBoxHeadless","*.so","*.r0","*.gc","components","nls"]:
        pisitools.insinto("/usr/share/VirtualBox","out/linux.x86/release/bin/%s" % file)

    # Kernel module
    pisitools.insinto("/lib/modules/%s/misc" % get.curKERNEL(), "out/linux.x86/release/bin/src/vboxdrv.ko")
    pisitools.insinto("/lib/modules/%s/misc" % get.curKERNEL(), "out/linux.x86/release/bin/src/vboxnetflt.ko")

    # Symlinks
    pisitools.dosym("/usr/bin/VBox.sh","/usr/bin/VirtualBox")
    pisitools.dosym("/usr/bin/VBox.sh","/usr/bin/VBoxManage")
    pisitools.dosym("/usr/bin/VBox.sh","/usr/bin/VBoxSDL")
    pisitools.dosym("/usr/bin/VBox.sh","/usr/bin/vditool")

    # Remove tests
    pisitools.remove("/usr/share/VirtualBox/tst*")

    # Desktop file
    pisitools.insinto("/usr/share/applications/","out/linux.x86/release/bin/VirtualBox.desktop")
    pisitools.insinto("/usr/share/pixmaps/","out/linux.x86/release/bin/VBox.png")
