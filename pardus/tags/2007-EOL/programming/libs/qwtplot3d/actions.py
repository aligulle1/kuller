#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="qwtplot3d"

def setup():
    shelltools.copytree("../qwtplot3d","../qwtplot3d-qt4")
    shelltools.system("qmake")
    shelltools.cd("../qwtplot3d-qt4")
    shelltools.system("qmake-qt4")

def build():
    autotools.make()

    shelltools.cd("../qwtplot3d-qt4")
    autotools.make()


def install():
    pisitools.insinto("%s/lib/" % get.qtDIR(),"lib/*")
    pisitools.insinto("%s/include/" % get.qtDIR(),"include/*")

    pisitools.insinto("/usr/share/doc/%s" % get.srcTAG(), "examples")

    shelltools.cd("../qwtplot3d-qt4")
    pisitools.insinto("/usr/qt/4/lib/","lib/*")
    pisitools.insinto("/usr/qt/4/include/","include/*")
