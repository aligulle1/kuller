#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="tellico"
shelltools.export("HOME", "%s" % get.workDIR())

def setup():
    cmaketools.configure("-DPOPPLER_QT4_INCLUDE_DIR=/usr/include -DPOPPLER_QT4_LIBRARIES=/usr/lib/libpoppler-qt4.so", installPrefix="/usr/kde/4", sourceDir=".")

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "TODO")
