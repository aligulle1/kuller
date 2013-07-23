#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import kde
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import get

WorkDir = "digikam-0.10.0-rc1"

def setup():
    shelltools.makedirs("build")
    shelltools.cd("build")

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
    for dir in ["16x16", "32x32", "48x48", "64x64", "128x128", "22x22", "scalable"]:
        for icon in ["view-object-histogram-linear", "view-object-histogram-logarithmic", "transform-crop-and-resize"]:
            try:
                if dir == "scalable":
                    pisitools.remove("/usr/kde/4/share/icons/oxygen/%s/actions/%s.svgz" % (dir, icon))
                else:
                    pisitools.remove("/usr/kde/4/share/icons/oxygen/%s/actions/%s.png" % (dir, icon))
            except:
                pass
