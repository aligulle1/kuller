#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

shelltools.export("INSTALL_ROOT", get.installDIR())

def setup():
    shelltools.system("./configure -prefix /%s \
                                   -libdir /usr/qt/4/lib \
                                   -headerdir /usr/qt/4/include \
                                   -qmake-bin /usr/qt/4/bin/qmake" % get.defaultprefixDIR())

def build():
    autotools.make()

def install():
    autotools.install()
