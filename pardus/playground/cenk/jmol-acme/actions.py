#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir="Acme"

def setup():
    shelltools.system("find . -name \*.class -delete")
    pisitools.makedirs("build")

def build():
    shelltools.system("/opt/sun-jdk/bin/javac -d build IntHashtable.java JPM/Encoders/GifEncoder.java JPM/Encoders/ImageEncoder.java JPM/Encoders/PpmEncoder.java")

    shelltools.system("/opt/sun-jdk/bin/jar cvf jmol-acme.jar -C build .")

def install():
    pisitools.insinto("/usr/share/java", "jmol-acme.jar")
