#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import get

def setup():
    cmaketools.configure("-DWANT_MONO=ON \
                          -DWANT_CORE=OFF \
                          -DWANT_QTCLIENT=OFF \
                          -DWITH_WEBKIT=OFF \
                          -DLINGUAS='da de en_US fr nb_NO tr_TR'")

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.insinto("usr/share/pixmaps", "src/icons/quassel/128x128/apps/quassel.png")

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "README", "gpl-?.0.txt")
