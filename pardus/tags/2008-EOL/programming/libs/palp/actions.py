#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "palp"

def build():
    pisitools.dosed("GNUmakefile", "^CFLAGS=.*$", "CFLAGS=%s" % get.CFLAGS())
    autotools.make()

def install():
    pisitools.dobin("*.x")

    pisitools.dodoc("COPYING")
