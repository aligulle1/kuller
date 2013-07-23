# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "partitionmanager-%s" % get.srcVERSION().replace("_", "-").upper()

def setup():
    shelltools.export("HOME", get.curDIR())
    cmaketools.configure("-DPARTMAN_KCM=ON \
                          -DPARTMAN_KPART=ON",
                         installPrefix="/usr/kde/4")

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("CHANGES", "COPYING", "README")
