#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "mt-st-%s" % get.srcVERSION()

def build():
    autotools.make("CC=%s" % get.CC())

def install():
    pisitools.dobin("mt")
    pisitools.dosbin("stinit")

    pisitools.doman("mt.1")
    pisitools.doman("stinit.8")
    pisitools.dodoc("stinit.def.examples", "README*")
