#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir = "hsqldb"

def setup():
    for jars in ["hsqldb","servlet"]:
        shelltools.unlink("lib/%s.jar" % jars)

def build():
    shelltools.export("JAVA_HOME", "/opt/sun-jdk")
    shelltools.cd("build")
    shelltools.system("ant jar")

def install():
    pisitools.insinto("/usr/share/java", "lib/hsqldb.jar")

    pisitools.dohtml("doc/*.html", "doc/guide/*", "doc/src/*")
    pisitools.dodoc("readme.txt", "doc/*.txt")
