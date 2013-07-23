#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "ManiaDrive-%s-linux-i386" % get.srcVERSION()
data = "/usr/share/%s" % get.srcNAME()
NoStrip = "/"

def install():
    pisitools.dodir("/usr/share")
    shelltools.copytree("game", "%s%s" % (get.installDIR(),data))
    pisitools.dodoc("README", "COPYING")

