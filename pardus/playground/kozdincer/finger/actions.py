#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2011 TUBITAK/BILGEM
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "bsd-finger-0.17"

def setup():
    autotools.rawConfigure("--installroot=%s \
                            --enable-ipv6" %(get.installDIR()))

def build():
    autotools.make()

def install():
    pisitools.dobin("finger/finger")
    pisitools.dosbin("fingerd/fingerd")
    pisitools.dosym("/usr/sbin/fingerd", "/usr/sbin/in.fingerd")
    pisitools.doman("finger/finger.1")
    pisitools.doman("fingerd/fingerd.8")
    pisitools.dosym("/usr/share/man/man8/fingerd.8", "/usr/share/man/man8/in.fingerd.8")
    pisitools.dodoc("README", "ChangeLog", "BUGS")
