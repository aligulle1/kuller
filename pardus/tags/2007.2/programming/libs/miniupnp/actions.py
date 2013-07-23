#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="miniupnpc-1.0-RC6"

def build():
    shelltools.export("OS_CFLAGS",get.CFLAGS())
    autotools.make()

def install():
    pisitools.dobin("upnpc")
    pisitools.dolib("libminiupnpc.so")

    for header in ["declspec","igd_desc_parse","miniupnpc","miniwget","upnpcommands","upnpreplyparse"]:
        pisitools.insinto("/usr/include/miniupnpc/","%s.h" % header)

    pythonmodules.install()

    pisitools.dodoc("Changelog.txt","README","LICENCE")
