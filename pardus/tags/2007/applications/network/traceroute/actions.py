#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005,2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "traceroute-1.4a12"

def setup():
    pisitools.dosed("configure.in", "t=\"generic\"", "t=\"linux\"")
    shelltools.export("LDFLAGS", "%s -Wl,-z,now"  % get.LDFLAGS())
    
    autotools.autoreconf()
    
    autotools.configure()

def build():
    autotools.make("LIBS=%s" % get.LDFLAGS())

def install():
    pisitools.dosbin("traceroute")
    pisitools.dosym("/usr/sbin/traceroute", "/bin/traceroute")
    pisitools.doman("traceroute.8")
    pisitools.dodoc("CHANGES", "INSTALL")
