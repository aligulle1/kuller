#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2006, TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "essential-%s" % get.srcVERSION().split("_", 1)[1]
NoStrip = "/"
dest = "essential"

def install():
    shelltools.chmod("*", mode = 0644)
    pisitools.dodir("/usr/lib/%s" % dest)
    pisitools.insinto("/usr/lib/%s" % dest, "*")

