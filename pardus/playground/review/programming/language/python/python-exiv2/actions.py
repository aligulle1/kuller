# -*- coding: utf-8 -*-
#
# Copyright 2011 TUBITAK/BILGEM
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import scons
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
     scons.make('CXX="%s" \
                 CXXFLAGS="%s" \
                 LDFLAGS="%s" ' % (get.CXX(), get.CXXFLAGS(), get.LDFLAGS()))

def install():
    scons.install("DESTDIR=%s install" % get.installDIR())
    scons.install("DESTDIR=%s doc" % get.installDIR())

    pisitools.dohtml("doc/html/*")
    pisitools.dodoc("README", "COPYING", "NEWS")

