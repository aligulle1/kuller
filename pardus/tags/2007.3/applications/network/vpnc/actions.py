#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2007 TUBITAK/UEKAE
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("Makefile", "CFLAGS=-W -Wall -O", "CFLAGS=%s" % get.CFLAGS())

def build():
    autotools.make()

def install():
    # bins.
    pisitools.dobin("vpnc")
    pisitools.dobin("vpnc-disconnect")
    pisitools.dobin("pcf2vpnc")
    pisitools.doexe("vpnc-script", "/etc/vpnc")

    # docs.
    pisitools.dodoc("README")
    pisitools.doman("vpnc.8")

    # conf.
    pisitools.insinto("/etc", "vpnc.conf")
