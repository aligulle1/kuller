#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import crosstools
from pisi.actionsapi import get
import os

def installi18n():
    for name in os.listdir('po'):
        if not name.endswith('.po'):
            continue
        lang = name[:-3]

        pisitools.domo("po/%s.po" % lang, lang, "pardus-python.mo")

# unfortunately compiling python modules failed, so I had to chose hard way.
def build():
    shelltools.system("mkdir -pv build/xorg")

    crosstools.environment["CFLAGS"] = "%(CFLAGS)s \
                                        -I%(RootDir)s/usr/include/python2.6 \
                                        -I../src -g3 -ggdb -fPIC" % crosstools.environment

    for file in ("xorg/capslock", "csapi"):
        crosstools.environment["file"] = file
        shelltools.system("%(CC)s %(CFLAGS)s -c pardus/%(file)s.c -o build/%(file)s.o" % crosstools.environment)

    crosstools.environment["file"] = "xorg/capslock"
    shelltools.system("%(CC)s -shared %(CFLAGS)s %(LDFLAGS)s build/%(file)s.o \
                       -lX11 -lpython2.6 -o build/%(file)s.so" % crosstools.environment)

    crosstools.environment["file"] = "csapi"
    shelltools.system("%(CC)s -shared %(CFLAGS)s %(LDFLAGS)s build/%(file)s.o \
                       -lpython2.6 -o build/%(file)s.so" % crosstools.environment)

def install():
    shelltools.makedirs("%s/usr/lib/pardus/pardus/xorg/" % get.installDIR())

    shelltools.copy("pardus/*py", "%s/usr/lib/pardus/pardus/" % get.installDIR() )
    shelltools.copy("pardus/xorg/*py", "%s/usr/lib/pardus/pardus/xorg/" % get.installDIR() )

    pisitools.insinto("/usr/lib/pardus/pardus/", "build/csapi.so")
    pisitools.insinto("/usr/lib/pardus/pardus/xorg", "build/xorg/capslock.so")

    installi18n()
    pisitools.dodoc("README")
