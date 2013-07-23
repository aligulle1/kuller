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

WorkDir = "kipi-plugins-kde4-0.2.0-beta1"

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

    shelltools.cd("..")
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README", "TODO")
