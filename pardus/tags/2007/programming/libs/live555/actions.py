#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005,2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="live"

def setup():
    shelltools.system("./genMakefiles linux")
    
def build():
    autotools.make()

def install():
    pisitools.dodir("/usr/lib")
    pisitools.dodir("/usr/include/live")
    
    shelltools.copy("BasicUsageEnvironment/include/*", "%s/usr/include/live/" % get.installDIR())
    shelltools.copy("BasicUsageEnvironment/*.a", "%s/usr/lib/" % get.installDIR())

    shelltools.copy("groupsock/include/*", "%s/usr/include/live/" % get.installDIR())
    shelltools.copy("groupsock/*.a", "%s/usr/lib/" % get.installDIR())

    shelltools.copy("liveMedia/include/*", "%s/usr/include/live/" % get.installDIR())
    shelltools.copy("liveMedia/*.a", "%s/usr/lib/" % get.installDIR())

    shelltools.copy("UsageEnvironment/include/*", "%s/usr/include/live/" % get.installDIR())
    shelltools.copy("UsageEnvironment/*.a", "%s/usr/lib/" % get.installDIR())

