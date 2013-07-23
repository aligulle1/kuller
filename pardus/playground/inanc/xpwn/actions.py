#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "posixninja-xpwn-1e685e6"

def setup():
    shelltools.makedirs("build")
    shelltools.cd("build")
    cmaketools.configure(installPrefix="/usr",sourceDir="..")

def build():
    shelltools.cd("build")
    cmaketools.make()

def install():
    shelltools.cd("build")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    for i in ("dfu-util", "dmg", "hdutil", "hfsplus", "ipsw", "ramdisk.dmg","xpwn", "xpwntool"):
        pisitools.domove("/usr/%s" % i, "/usr/bin")

    for j in ("bundles", "FirmwareBundles"):
        pisitools.domove("/usr/%s" % j, "/usr/share/xpwn")

    pisitools.domove("/usr/*.txt", "/usr/share/doc/xpwn")
