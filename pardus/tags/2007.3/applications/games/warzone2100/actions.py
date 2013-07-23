#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import libtools
from pisi.actionsapi import get


def setup():
    pisitools.dosed("Makefile.am", "\$\(datadir\)", "/usr/share")
    pisitools.dosed("Makefile.am", "/usr/share/icons", "/usr/share/pixmaps")
    shelltools.touch("NEWS")

    # shelltools.export("AT_M4DIR", "m4")
    # libtools.libtoolize("--copy --force")
    # shelltools.system("./autogen.sh")

    autotools.configure("--disable-dependency-tracking \
                         --with-ogg=/usr \
                         --with-mp3=/usr \
                         --enable-ogg \
                         --enable-mp3 \
                         --disable-debug")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    # pisitools.dodoc("AUTHORS", "README", "TODO", "ChangeLog", "COPYING*")

    pisitools.rename("/usr/share/icons", "pixmaps")
    pisitools.removeDir("/usr/share/applications")

