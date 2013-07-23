#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "dmz-cursor-theme-%s" % get.srcVERSION()

def install():
    shelltools.cd("DMZ-White/pngs")
    shelltools.system("./make.sh")

    shelltools.cd("../../DMZ-Black/pngs")
    shelltools.system("./make.sh")

    shelltools.cd("../..")

    pisitools.insinto("/usr/share/icons/DMZ", "DMZ-White/*.theme")
    pisitools.insinto("/usr/share/icons/DMZ/cursors", "DMZ-White/xcursors/*")

    pisitools.insinto("/usr/share/icons/DMZ-AA", "DMZ-Black/*.theme")
    pisitools.insinto("/usr/share/icons/DMZ-AA/cursors", "DMZ-Black/xcursors/*")

    pisitools.dodoc("debian/copyright")
