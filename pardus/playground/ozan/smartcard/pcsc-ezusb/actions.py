#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "%s-%s/%s" % (get.srcNAME(), get.srcVERSION(), get.ARCH())
NoStrip = ["/"]

def install():
    pisitools.dodir("/usr/lib/pcsc/drivers/ezusb.bundle/Contents/Linux")
    pisitools.dobin("ezusb.so", "/usr/lib/pcsc/drivers/ezusb.bundle/Contents/Linux")
