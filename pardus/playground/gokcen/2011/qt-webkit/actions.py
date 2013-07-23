# -*- coding: utf-8 -*-
#
# Copyright 2011 TUBITAK/BILGEM
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "webkit-qtwebkit"

def build():
    shelltools.system("Tools/Scripts/build-webkit --makeargs=\"%s\" \
                                                  --qt \
                                                  --release" % (get.makeJOBS()))

def install():
    shelltools.system("make install INSTALL_ROOT='%s' -C WebKitBuild/Release" % get.installDIR())

    pisitools.dodoc("ChangeLog")
