#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

import os

# Workdir changes all the time
# WorkDir = "glest_source_%s" % get.srcVERSION()
WorkDir = "./"

def fixperms(target):
    for root, dirs, files in os.walk(target):
        for name in dirs:
            shelltools.chmod(os.path.join(root, name), 0755)
        for name in files:
            shelltools.chmod(os.path.join(root, name), 0644)

def dos2unix(target):
    for root, dirs, files in os.walk(target):
        for name in files:
            pisitools.dosed(os.path.join(root, name), "\r")

def setup():
    for d in shelltools.ls("./"):
        if shelltools.isDirectory(d):
            fixperms(d)

    # dos2unix("source")
    dos2unix("mk")

    shelltools.cd("mk/linux")
    shelltools.chmod("autogen.sh", 0755)
    shelltools.system("./autogen.sh")

    shelltools.unlink("glest_map_editor")
    dos2unix("../")

    pisitools.dosed("Jamrules", "^COMPILER_CFLAGS_optimize \+=.*", "COMPILER_CFLAGS_optimize += %s ;" % get.CFLAGS())
    pisitools.dosed("Jamrules", "^COMPILER_C\+\+FLAGS_optimize \+=.*", "COMPILER_C++FLAGS_optimize += %s ;" % get.CXXFLAGS())
    pisitools.dosed("Jamrules", "^COMPILER_LFLAGS_optimize \+=.*", "COMPILER_LFLAGS_optimize += %s ;" % get.LDFLAGS())

    autotools.configure("--with-ogg \
                         --with-vorbis \
                         --with-libOpenAL \
                         --with-wx-config=disabled_wx \
                         --with-x")

def build():
    shelltools.cd("mk/linux")
    shelltools.system("jam")

def install():
    pisitools.doexe("mk/linux/glest", "/usr/share/glest/lib")
    pisitools.dodoc("docs/README*", "docs/license.txt")

