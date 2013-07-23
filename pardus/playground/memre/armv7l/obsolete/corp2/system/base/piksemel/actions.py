#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt
#

from pisi.actionsapi import crosstools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    shelltools.system("mkdir -pv build/xorg")
    crosstools.environment["CFLAGS"] = "%(CFLAGS)s -fPIC -I%(RootDir)s/usr/include/python2.6" % crosstools.environment
    crosstools.environment["LDFLAGS"] = "%(LDFLAGS)s -L%(RootDir)s/usr/lib/ -lpython2.6 -lX11" % crosstools.environment

    for file in ("iksemel", "pyiks"):
        crosstools.environment["file"] = file
        shelltools.system("%(CC)s %(CFLAGS)s -c src/%(file)s.c -o build/%(file)s.o" % crosstools.environment)
    shelltools.system("%(CC)s -shared %(CFLAGS)s %(LDFLAGS)s build/iksemel.o build/pyiks.o -o build/piksemel.so" % \
                       crosstools.environment)

def install():
    shelltools.makedirs("%s/usr/lib/pardus/" % get.installDIR())

    pisitools.insinto("/usr/lib/pardus/", "build/piksemel.so")

    pisitools.dodoc("README")
