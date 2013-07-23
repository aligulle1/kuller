#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir ="DSDP%s" % get.srcVERSION()

def build():
    shelltools.export("DSDPROOT", get.curDIR())
    autotools.make()

def install():
    pisitools.dolib("lib/libdsdp.so")
    pisitools.insinto("/usr/include","include/*.h")

    pisitools.dodoc("Readme", "docs/*.pdf")
