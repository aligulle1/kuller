#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir = "Jimmac"

def install():
    pisitools.dodir("/usr/share/cursors/xorg-x11/Jimmac/")
    shelltools.copytree("jimmac/cursors/","%s/usr/share/cursors/xorg-x11/Jimmac/cursors" % get.installDIR(), True)
