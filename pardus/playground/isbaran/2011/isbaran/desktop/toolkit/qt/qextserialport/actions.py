#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "qextserialport_%s" % get.srcVERSION()

def setup():
    shelltools.system("qmake-qt4 qextserialport.pro")
    shelltools.cd("src")
    shelltools.system("qmake-qt4 src.pro")

def build():
    autotools.make("-j1")

    shelltools.cd("src")
    autotools.make("-j1")

    shelltools.cd("../")

    shelltools.system("doxygen Doxyfile")
    shelltools.system("doxygen doc/*.dox")

def install():
    autotools.install()

    pisitools.dolib("src/build/*", destinationDirectory="%s/lib" % get.qtDIR())

    pisitools.dohtml("html/*")

    pisitools.insinto("%s/qextserialport/examples" % get.docDIR(), "examples/*")

