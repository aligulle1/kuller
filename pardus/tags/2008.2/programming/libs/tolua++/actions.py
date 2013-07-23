#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import scons
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    scons.make('CC="%s" \
                CCFLAGS="%s" \
                LINK="%s" \
                LINKFLAGS="%s"'
                % (get.CC(), get.CFLAGS(), get.CC(), get.LDFLAGS()))

def install():
    for dirs in ["bin", "include", "lib"]:
        pisitools.insinto("/usr", dirs)

    # No sconsign files
    pisitools.remove("/usr/*/.sconsign")

    pisitools.dohtml("doc/*")
    pisitools.dodoc("README*")
