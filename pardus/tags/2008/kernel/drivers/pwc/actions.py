#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="pwc-v4l2-20080322-042701"

def setup():
    pisitools.dosed("Makefile", "\$\(shell uname -r\)", get.curKERNEL())

def build():
    shelltools.export("ARCH", "i386")
    autotools.make("KSRC=/lib/modules/%s/source" % get.curKERNEL())

def install():
    pisitools.insinto("/lib/modules/%s/extra" % get.curKERNEL(), "*.ko")
