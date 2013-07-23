#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="atl2-%s/src" % get.srcVERSION()

def setup():
    pisitools.dosed("Makefile", "BUILD_KERNEL=.*", "BUILD_KERNEL = %s" % get.curKERNEL())
    pisitools.dosed("Makefile", "shell uname -r", "shell echo %s" % get.curKERNEL())

def build():
    autotools.make("BUILD_KERNEL=/lib/modules/%s/build default" % get.curKERNEL())

def install():
    pisitools.insinto("/lib/modules/%s/extra" % get.curKERNEL(), "*.ko")

    shelltools.cd("..")
    pisitools.doman("atl2.7")
    pisitools.dodoc("COPYING", "readme", "release_note.txt")
