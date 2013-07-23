#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "SYMPOW-%s" % get.srcVERSION()

def setup():
    shelltools.move("Configure","configure")
    autotools.rawConfigure()

def build():
    autotools.make()

def install():
    pisitools.dobin("sympow")

    pisitools.insinto("/usr/lib/sympow","*.gp")
    pisitools.insinto("/usr/lib/sympow","new_data")

    pisitools.dodoc("COPYING", "README")
