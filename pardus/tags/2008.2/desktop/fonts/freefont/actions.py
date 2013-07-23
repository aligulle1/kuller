#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "freefont-%s" % get.srcVERSION().split("_")[1]

def install():
    pisitools.insinto("/usr/share/fonts/freefont/", "*.ttf")

    pisitools.dodoc("AUTHORS", "ChangeLog", "CREDITS", "README","COPYING")
