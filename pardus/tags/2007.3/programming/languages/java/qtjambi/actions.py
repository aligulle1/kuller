#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="qtjambi-gpl-src-%s_01" % get.srcVERSION()

def setup():
    shelltools.chmod("build.sh")
    pisitools.dosed("build.sh","VERSION", get.srcVERSION())

def build():
    shelltools.system("./build.sh")

def install():
    pisitools.insinto("/usr/share/java","qtjambi-%s.jar" % get.srcVERSION())
    pisitools.dosym("/usr/share/java/qtjambi-%s.jar" % get.srcVERSION(), "/usr/share/java/qtjambi.jar")

    pisitools.insinto("/usr/qt/4/plugins","plugins/*")
    pisitools.insinto("/usr/qt/4/lib","lib/*")
    pisitools.insinto("/usr/qt/4/include","include/*")
    pisitools.insinto("/usr/qt/4/bin","bin/juic")

    for data in ["demos","examples","images","launcher","manualtests"]:
        pisitools.insinto("/usr/share/doc/%s/com/trolltech" % get.srcTAG(), "com/trolltech/%s" % data)

    pisitools.dodoc("README","changes*","LICENSE*")
