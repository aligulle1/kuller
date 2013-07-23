#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get

WorkDir="miniupnpc-1.0-RC11"

def build():
    shelltools.export("OS_CFLAGS",get.CFLAGS())
    autotools.make()

def install():
    autotools.install("PREFIX=%s" % get.installDIR())
    pisitools.insinto("/usr/bin","upnpc-static","upnpc")

    pythonmodules.install()

    # No static libs
    pisitools.remove("/usr/lib/*.a")

    pisitools.doman("man3/miniupnpc.3")
    pisitools.dodoc("Changelog.txt","README","LICENCE")
