#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

WorkDir="xml-xalan/c"

def setupVars():
    shelltools.export("XERCESCROOT","/usr")
    shelltools.export("XALANCROOT","%s" % get.curDIR())
    shelltools.export("ICUROOT","/usr")
    shelltools.export("XALAN_USE_ICU","true")

def setup():
    setupVars()
    shelltools.system("./runConfigure -plinux \
                       -cgcc \
                       -P/usr \
                       -ticu")
def build():
    setupVars()
    autotools.make()

def install():
    setupVars()
    autotools.rawInstall("DESTDIR=%s install" % get.installDIR())

    # This comes from ICU
    pisitools.remove("/usr/lib/libicui18n.*")
