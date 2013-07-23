#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005, 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="pwc-v4l2-20060926-042701"

def build():
    shelltools.export("ARCH", "i386")
    autotools.make("KSRC=/usr/src/linux")

def install():
    pisitools.insinto("/lib/modules/%s/extra" % get.curKERNEL(), "*.ko")
