#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="qwt-%s" % get.srcVERSION()

def setup():
    shelltools.system("qmake-qt4 qwt.pro")

def build():
    autotools.make("-j1")


def install():
    pisitools.insinto("%s/lib/" % get.qtDIR(),"lib/*")
    pisitools.insinto("%s/include/qwt" % get.qtDIR() ,"src/*.h")

    pisitools.insinto("/usr/share/doc/%s" % get.srcNAME(), "examples")
    pisitools.insinto("/usr/share/doc/%s" % get.srcNAME(), "doc/html")
    pisitools.doman("doc/man/man3/*.3")

    # remove md5
    pisitools.remove("/usr/share/doc/%s//html/*.md5" % get.srcNAME())

    pisitools.insinto("%s/plugins/designer" % get.qtDIR(),"designer/plugins/designer/*.so")

