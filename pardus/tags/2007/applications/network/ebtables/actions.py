#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "ebtables-v2.0.6"

def build():
    autotools.make()

def install():
    pisitools.dodir("/sbin")
    autotools.rawInstall("MANDIR=%s/usr/share/man ETHERTYPESPATH=%s/etc/ BINPATH=%s/sbin/" % (get.installDIR(), get.installDIR(), get.installDIR()))
