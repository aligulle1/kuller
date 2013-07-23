#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir="pisi-developer-tools-"+get.srcVERSION()

def install():
    pisitools.insinto("/usr/kde/4/share/kde4/services/ServiceMenus/", "*.desktop")
    pisitools.insinto("/usr/kde/4/share/apps/pisi-developer-tools/", "*")