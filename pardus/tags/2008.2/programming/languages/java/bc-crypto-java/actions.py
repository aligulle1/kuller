#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007,2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="crypto-140"

def build():
    shelltools.system("sh build1-6")

def install():
    for lib in ["bcmail","bcprov","bcpg","bctsp","bctest"]:
        pisitools.insinto("/usr/share/java", "build/artifacts/jdk1.6/jars/%s-jdk16-140.jar" % lib, "%s.jar" % lib)

    pisitools.dohtml("*.html")
