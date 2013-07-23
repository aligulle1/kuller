#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.copy("/usr/share/gettext/config.rpath", ".")

    autotools.autoreconf("-vfi")
    autotools.configure("--disable-static \
                         --disable-dependency-tracking \
                         --disable-silent-rules \
                         --enable-py-build-only \
                         --enable-gnet \
                         --enable-sqlite \
                         --with-python=/usr/bin/python")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    #pisitools.remove("/usr/lib/gcompris/libgoocanvas.so*")

    pisitools.dodoc("ABOUT-NLS", "AUTHORS", "ChangeLog", "COPYING", "NEWS", "README*", "THANKS", "TODO")
