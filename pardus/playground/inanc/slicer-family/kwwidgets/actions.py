#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import get
from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools

WorkDir = "KWWidgets-HEAD-cvs"

def setup():
    cmaketools.configure("-DCMAKE_INSTALL_PREFIX=%s/usr \
                          -DBUILD_SHARED_LIBS=ON \
                          -DCMAKE_SKIP_RPATH=ON \
                          -DKWWidgets_BUILD_TESTING=OFF"% get.installDIR())

def build():
    cmaketools.make()

def install():
    cmaketools.install()

    pisitools.dobin("bin/KWConvertImageToHeader")
