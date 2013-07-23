#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

shelltools.export("HOME", get.workDIR())

def setup():
    shelltools.makedirs("build")
    shelltools.cd("build")

    cmaketools.configure("-DBUILD_EVERYTHING=ON", installPrefix="/usr/kde/4", sourceDir="..")
    cmaketools.configure("-DEIGEN2_INCLUDE_DIR=/usr/include/eigen2 \
                          -DBUILD_kexi:BOOL=ON \
                          -DBUILD_kchart:BOOL=ON ", installPrefix="/usr/kde/4", sourceDir="..")

def build():
    shelltools.cd("build")
    cmaketools.make()

def install():
    pisitools.dodoc("COPYING*", "README", "doc/status.txt")

    shelltools.cd("build")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.remove("/usr/kde/4/share/kde4/services/ServiceMenus/kivio_konqi.desktop")
