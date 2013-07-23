#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

NoStrip = ["/"]

def setup():
    for package in shelltools.ls("."):
        shelltools.cd(package)
        autotools.configure("--with-encodingsdir=/usr/share/fonts/encodings \
                             --with-mapfiles=/usr/share/fonts/util \
                             --with-top-fontdir=/usr/share/fonts")
        shelltools.cd("../")

def build():
    for package in shelltools.ls("."):
        shelltools.cd(package)
        autotools.make()
        shelltools.cd("../")

def install():
    for package in shelltools.ls("."):
        shelltools.cd(package)
        autotools.rawInstall("DESTDIR=%s" % get.installDIR())
        shelltools.cd("../")

    # ugly hack...
    pisitools.domove("/usr/lib/X11/fonts/100dpi/*", "/usr/share/fonts/100dpi/")
    pisitools.domove("/usr/lib/X11/fonts/75dpi/*", "/usr/share/fonts/75dpi/")
    pisitools.domove("/usr/lib/X11/fonts/misc/*", "/usr/share/fonts/misc")
    pisitools.removeDir("/usr/lib/")
