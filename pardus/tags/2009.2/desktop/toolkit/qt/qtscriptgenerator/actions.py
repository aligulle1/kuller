#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="qtscriptgenerator-src-%s" % get.srcVERSION()

def setup():
    shelltools.cd("generator")
    shelltools.system("qmake-qt4 generator.pro")
    shelltools.cd("../qtbindings")
    shelltools.system("qmake-qt4 qtbindings.pro")

def build():
    shelltools.cd("generator")
    autotools.make("-j1")
    shelltools.system("QTDIR=/usr/qt/4 ./generator --include-paths='/usr/qt/4/include/'")

    shelltools.cd("../qtbindings")
    autotools.make("-j1")

def install():
    pisitools.insinto("/usr/qt/4/plugins/script", "plugins/script/*")
    pisitools.insinto("%s/qtscriptgenerator" % get.docDIR(), "doc/*")

    pisitools.dodoc("LICENSE.GPL")
