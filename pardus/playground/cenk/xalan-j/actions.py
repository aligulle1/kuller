#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir="xalan-j_2_7_1"

def build():
    shelltools.system("ant xalan-interpretive.jar")

def install():
    pisitools.insinto("/usr/share/java/", "build/*.jar")

    pisitools.dohtml("readme.html")
    pisitools.dodoc("*.txt", "KEYS")
