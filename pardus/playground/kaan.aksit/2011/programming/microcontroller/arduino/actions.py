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

def build():
    shelltools.export("JAVA_HOME","/opt/sun-jre")
    shelltools.system("ant")

def install():
    pisitools.dodir("/usr/share/arduino")
    pisitools.dodir("/usr/bin")

    shelltools.copy("%s/%s/linux/arduino-add-groups" % (get.workDIR(),WorkDir),"%s/usr/share/arduino/arduino-add-groups" % get.installDIR())
    shelltools.chmod("%s/usr/share/arduino/arduino-add-groups" % get.installDIR(), 0775)

    shelltools.copy("%s/%s/linux/work/*" % (get.workDIR(),WorkDir),"%s/usr/share/arduino" % get.installDIR())

    pisitools.dosym("/usr/share/arduino/arduino", "/usr/bin/arduino")

    pisitools.dodoc("%s/usr/share/arduino/revisions.txt" % get.installDIR())

    if get.ARCH() == "x86_64":
        pisitools.remove("/usr/share/arduino/lib/RXTXcomm.jar")
        pisitools.remove("/usr/share/arduino/lib/librxtxSerial.so")

        shelltools.copy("%s/arduinox64/arduino-1.0/lib/RXTXcomm.jar" % (get.workDIR()),"%s/usr/share/arduino/lib" % get.installDIR())
        shelltools.copy("%s/arduinox64/arduino-1.0/lib/librxtxSerial.so" % (get.workDIR()),"%s/usr/share/arduino/lib" % get.installDIR())
    elif get.ARCH() == "i686":
        pisitools.remove("/usr/share/arduino/lib/librxtxSerial64.so")
        pisitools.remove("/usr/share/arduino/hardware/tools/avrdude64")        
