#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005, 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

import os
from os.path import join

WorkDir = "glest_source_2.0.0"

def dos2unix(target):
    for root, dirs, files in os.walk(target):
        for name in files:
            pisitools.dosed(join(root, name), "\r")

def setup():
    shelltools.cd("..")
    for root, dirs, files in os.walk(WorkDir):
        for name in dirs:
            shelltools.chmod(join(root, name), 0755)
        for name in files:
            shelltools.chmod(join(root, name), 0644)

    shelltools.cd(WorkDir)
    # dos2unix("source")
    dos2unix("mk")

    shelltools.cd("mk/linux")
    shelltools.chmod("autogen.sh", 0755)
    shelltools.system("./autogen.sh")

    shelltools.cd("../..")
    shelltools.unlink("mk/linux/glest_map_editor")

    dos2unix("mk")

    # pisitools.dosed("mk/linux/Jamrules", "COMPILER_CFLAGS_optimize \+= -O3 -g3", "COMPILER_CFLAGS_optimize \+= %s" % get.CFLAGS()) 
    # pisitools.dosed("mk/linux/Jamrules", "COMPILER_C\+\+FLAGS_optimize \+= -O3 -g3", "COMPILER_CFLAGS_optimize \+= %s" % get.CXXFLAGS()) 

    shelltools.cd("mk/linux")
    autotools.configure("--with-ogg \
                         --with-vorbis \
                         --with-libOpenAL \
                         --with-x")

def build():
    shelltools.cd("mk/linux")
    shelltools.system("jam")
    
def install():
    pisitools.dodoc("docs/README*", "docs/license.txt")
    shelltools.cd("mk/linux")
    pisitools.doexe("glest", "/usr/share/glest/lib")

