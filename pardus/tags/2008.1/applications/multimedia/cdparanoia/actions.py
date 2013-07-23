#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import libtools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "cdparanoia-III-10pre0"

def setup():
    shelltools.export("CC", get.CC())
    shelltools.export("CXX", get.CXX())
    shelltools.export("RANLIB", get.RANLIB())
    shelltools.export("AR", get.AR())

    shelltools.move("configure.guess", "config.guess")
    shelltools.move("configure.sub", "config.sub")

    shelltools.export("CFLAGS", "%s -I%s/interface" % (get.CFLAGS(), get.curDIR()))
    shelltools.export("CXXLAGS", "%s -I%s/interface" % (get.CXXFLAGS(), get.curDIR()))

    autotools.autoconf()
    libtools.gnuconfig_update()
    autotools.configure()

def build():
    shelltools.export("CC", get.CC())
    shelltools.export("CXX", get.CXX())
    shelltools.export("RANLIB", get.RANLIB())
    shelltools.export("AR", get.AR())

    autotools.make('OPT="%s"' % get.CFLAGS())

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # No static libs
    pisitools.remove("/usr/lib/*.a")

    pisitools.dodoc("FAQ.txt", "README")
