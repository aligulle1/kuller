#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import libtools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get

def setup():
    pisitools.dosed("swig/python/Makefile.in", "PYTHON\=\$\(PYTHON\)\ \$\(\py\_compile\).*", "wait; \\\\")
    autotools.configure("--with-pic \
                         --disable-static \
                         --enable-inline \
                         --enable-cassert \
                         --enable-swig \
                         --enable-python \
                         --enable-ruby")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "COPYING", "ChangeLog", "INSTALL", "NEWS", "README", "TODO")
