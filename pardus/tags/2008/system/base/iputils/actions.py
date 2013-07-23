#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="iputils-s%s" % get.srcVERSION()

def build():
    autotools.make()

#    shelltools.cd("doc")
#    autotools.make("man")

def install():
    for app in ["ping","ping6"]:
        pisitools.dobin(app)

    for app in ["clockdiff","arping","rdisc","tracepath","tracepath6","traceroute6"]:
        pisitools.dosbin(app)

    shelltools.chmod("%s/usr/bin/ping" % get.installDIR(), 04711)
    shelltools.chmod("%s/usr/bin/ping6" % get.installDIR(), 04711)

    # man conflict with tftp
    pisitools.remove("/usr/share/man/man8/tftpd.8")

#    pisitools.doman("doc/*.8")
    pisitools.dodoc("RELNOTES")
