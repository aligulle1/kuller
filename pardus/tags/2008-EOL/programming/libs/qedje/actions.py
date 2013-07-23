#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.system("qmake-qt4 qedje.pro PREFIX=/usr")

def build():
    autotools.make('CFLAGS="%s" CXXFLAGS="%s" CC="%s" CXX="%s"' 
                 % (get.CFLAGS(), get.CXXFLAGS(), get.CC(), get.CXX()))

def install():
    autotools.rawInstall("INSTALL_ROOT=%s" % get.installDIR())
    pisitools.dodoc("README", "AUTHORS.libedje", "COPYING", "NEWS", "TODO")
    pisitools.dosed("%s/usr/lib/libqedje.prl" % get.installDIR(), "^QMAKE_PRL_BUILD_DIR.*", '')

