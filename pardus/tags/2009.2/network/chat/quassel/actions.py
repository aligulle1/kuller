#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

shelltools.export("HOME", get.workDIR())

def setup():
    cmaketools.configure("-DWANT_MONO=ON \
                          -DWANT_CORE=ON \
                          -DWANT_QTCLIENT=ON \
                          -DWITH_OPENSSL=ON \
                          -DWITH_WEBKIT=ON \
                          -DWITH_PHONON=ON \
                          -DWITH_KDE=ON \
                          -DWITH_OXYGEN=ON \
                          -DWITH_LIBINDICATE=OFF \
                          -DEMBED_DATA=OFF \
                          -DDATA_INSTALL_DIR=/usr/kde/4/share/apps \
                          -DLINGUAS='cs da de en_US fr hu it nb_NO tr_TR ru'")

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dobin("scripts/manageusers.py")

    pisitools.dodir("/var/cache/quassel")
    shelltools.chmod("%s/var/cache/quassel" % get.installDIR(), 0770)

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "README", "gpl-?.0.txt")
