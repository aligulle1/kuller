#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
 
WorkDir = "."
NoStrip = "/"

datadir = "/usr" 
 
def install():
	pisitools.insinto('/', '*')
	pisitools.dobin("/usr/lib/pidgin")
	pisitools.dobin("/usr/lib/purple-2")
	pisitools.dobin("/usr/share/pixmaps/pidgin/protocols")

