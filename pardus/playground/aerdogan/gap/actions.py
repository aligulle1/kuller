#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "gap4r4"
files = ["etc","grp","lib","pkg","prim","small","trans","tst"]

def setup():
    autotools.configure()

def build():
    autotools.make()

def install():
    pisitools.dobin("bin/i686-pc-linux-gnu-i686-pc-linux-gnu-gcc/gap")

    for data in files:
        pisitools.insinto("/usr/share/%s" % get.srcNAME(),data)

    pisitools.insinto("/usr/share/doc/%s" % get.srcTAG(),"doc/*")
    pisitools.dodoc("description*", "README")
