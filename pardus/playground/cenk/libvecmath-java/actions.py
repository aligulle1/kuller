#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "vecmath1.2-%s" % get.srcVERSION()

def setup():
    shelltools.makedirs("build")

def build():
    shelltools.system("/opt/sun-jdk/bin/javac -d build `find javax -name *.java | xargs`")
    shelltools.system("/opt/sun-jdk/bin/jar cvf libvecmath.jar -C build .")

def install():
    pisitools.insinto("/usr/share/java", "libvecmath.jar")

    pisitools.dodoc("README", "CHANGES")
