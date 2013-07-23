#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="pwc-v4l2-20070616-042702"

def setup():
    pisitools.dosed("Makefile", "\$\(shell uname -r\)", get.curKERNEL())

def build():
    shelltools.export("ARCH", "i386")
    autotools.make("KSRC=/usr/src/linux-%s" % get.curKERNEL())

def install():
    pisitools.insinto("/lib/modules/%s/extra" % get.curKERNEL(), "*.ko")
