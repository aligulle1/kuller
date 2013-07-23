#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "jakarta-regexp-%s" % get.srcVERSION()

def setup():
    pisitools.unlink("jakarta-regexp-%s.jar" % get.srcVERSION())

def build():
    shelltools.system("ant")

def install():
    pisitools.insinto("/usr/share/java", "build/jakarta-regexp-*.jar", "regexp.jar")

    pisitools.dodoc("LICENSE", "README", "NOTICE")
