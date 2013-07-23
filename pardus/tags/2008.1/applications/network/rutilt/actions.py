#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "RutilTv%s" % get.srcVERSION()

def setup():
    shelltools.system("./configure.sh \
                            --force \
                            --launcher=external \
                            --prefix=/usr \
                            --kernel_sources=/usr")

def build():
    autotools.make('-j1 OPTIONS="%s"' % get.CXXFLAGS())

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dosym("/usr/share/icons/hicolor/128x128/apps/rutilt.png", "/usr/share/pixmaps/rutilt.png")

    pisitools.dodoc("AUTHORS", "COPYING", "README*")
