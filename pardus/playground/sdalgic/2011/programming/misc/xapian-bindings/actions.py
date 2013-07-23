#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.export("CPPFLAGS", "%s -I/opt/sun-jdk/include" % get.CXXFLAGS())
    shelltools.export("JAVA_HOME", "/opt/sun-jdk")
    autotools.autoreconf("-vfi")
    autotools.configure("--with-python \
                         --with-pic \
                         --with-ruby \
                         --with-perl \
                         --with-tcl")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README", "TODO")
