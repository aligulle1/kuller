#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import kde
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import get

WorkDir = "digikam-0.10.0_beta3_859144"

def setup():
    shelltools.makedirs("build")
    shelltools.cd("build")

    shelltools.export("PKG_CONFIG_PATH", "/usr/kde/4/lib/pkgconfig")

    cmaketools.configure("-DCMAKE_LIBRARY_PATH=/usr/kde/4/lib \
                          -DCMAKE_INCLUDE_PATH=/usr/kde/4/include \
                          -DCMAKE_BUILD_TYPE=release", installPrefix="/usr/kde/4", sourceDir="..")

def build():
    shelltools.cd("build")
    cmaketools.make()

def install():
    shelltools.cd("build")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    # These files conflict with kdebase4-runtime.
    # TODO: Remove them from kdebase4-runtime after..
    for dir in ["16x16", "32x32", "48x48", "64x64", "128x128", "22x22"]:
        pisitools.remove("/usr/kde/4/share/icons/oxygen/%s/apps/digikam.png" % dir)

    pisitools.remove("/usr/kde/4/share/icons/oxygen/scalable/apps/digikam.svgz")

