#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def build():
    shelltools.system("/opt/sun-jdk/bin/javac -d . Main.java")
    shelltools.system("/opt/sun-jdk/bin/jar cvf jlex.jar JLex/")

def install():
    pisitools.insinto("/usr/share/java", "jlex.jar")

    pisitools.dodoc("LICENSE")
