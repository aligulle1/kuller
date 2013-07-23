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
flags = "%s -I%s/%s/interface" % (get.CFLAGS(), get.workDIR(), WorkDir)

def setup():
    shelltools.export("CC", get.CC())
    shelltools.export("CXX", get.CXX())
    shelltools.export("CFLAGS", flags)
    shelltools.export("CXXLAGS", flags)

    shelltools.move("configure.guess", "config.guess")
    shelltools.move("configure.sub", "config.sub")

    autotools.autoconf()
    libtools.gnuconfig_update()
    libtools.libtoolize("--force --install")
    autotools.configure()

def build():
    shelltools.export("CC", get.CC())
    shelltools.export("CXX", get.CXX())

    autotools.make('OPT="%s"' % flags)

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # No static libs
    pisitools.remove("/usr/lib/*.a")

    pisitools.dodoc("FAQ.txt", "README")
