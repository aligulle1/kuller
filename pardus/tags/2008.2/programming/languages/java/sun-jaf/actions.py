#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007,2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir="glassfish/jaf"

def build():
    shelltools.export("JAVA_HOME", "/opt/sun-jdk")
    shelltools.system("ant jar")

def install():
    pisitools.insinto("/usr/share/java", "build/release/activation.jar")

    pisitools.dodoc("README.txt", "LICENSE.txt", "RELNOTES.txt")
