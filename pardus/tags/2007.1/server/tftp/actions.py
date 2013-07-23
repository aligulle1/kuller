#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005, 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "tftp-hpa-0.46"

def setup():
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.rawInstall("INSTALLROOT=%s" % get.installDIR())
    pisitools.dodir("/tftpboot")
    pisitools.dodoc("README", "CHANGES")
