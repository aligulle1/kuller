#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2011 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt
#

from pisi.actionsapi import shelltools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

WorkDir = "arduino-%s/build" % get.srcVERSION()

def setup():
    pass

def build():
    shelltools.export("JAVA_HOME","/opt/sun-jre")
    shelltools.system("ant")

def install():
    shelltools.makedirs("%s/usr/share/arduino" % get.installDIR())
    shelltools.makedirs("%s/usr/bin" % get.installDIR())
    shelltools.copy("%s/%s/linux/work/*" % (get.workDIR(),WorkDir),"%s/usr/share/arduino" % get.installDIR())
    pisitools.dosym("/usr/share/arduino/arduino", "/usr/bin/arduino")
    if get.ARCH() == "x86_64":
        pisitools.remove("/usr/share/arduino/lib/RXTXcomm.jar")
        pisitools.remove("/usr/share/arduino/lib/librxtxSerial.so")
        shelltools.copy("%s/arduino-%s/lib/RXTXcomm.jar" % (get.workDIR(),get.srcVERSION()),"%s/usr/share/arduino/lib" % get.installDIR())
        shelltools.copy("%s/arduino-%s/lib/librxtxSerial.so" % (get.workDIR(),get.srcVERSION()),"%s/usr/share/arduino/lib" % get.installDIR())
         
