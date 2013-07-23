#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "fingerprint-gui-%s" % get.srcVERSION()
builddir = "build"

def setup():
    shelltools.system("qmake PREFIX=/usr LIBPOLKIT_QT=LIBPOLKIT_QT_1_1")

def build():
    autotools.make()

def install():
    autotools.rawInstall("INSTALL_ROOT=%s" % get.installDIR())
    pisitools.dodoc("CHANGELOG", "README", "COPYING")
    #shelltools.system("make install-upek")

