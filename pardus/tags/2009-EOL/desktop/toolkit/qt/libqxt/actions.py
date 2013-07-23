#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = get.srcNAME()
shelltools.export("INSTALL_ROOT", get.installDIR())

def setup():
    autotools.rawConfigure("-prefix /usr \
                            -libdir /usr/qt/4/lib \
                            -headerdir /usr/qt/4/include \
                            -qmake-bin /usr/qt/4/bin/qmake")

    # Don't use the installed headers as they avoid the package from building
    # when the installed package is old.
    pisitools.dosed("src/*/Makefile", "-I%s/include/QxtCore" % get.qtDIR(), "")


def build():
    autotools.make()

def install():
    autotools.install("INSTALL_ROOT=%s" % get.installDIR())

    pisitools.removeDir("/usr/doc")
