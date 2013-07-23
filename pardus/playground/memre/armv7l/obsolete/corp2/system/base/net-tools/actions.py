#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import crosstools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("Makefile", "(?m)^(COPTS =.*)", "COPTS = %s -fPIE" % get.CFLAGS())
    pisitools.dosed("Makefile", "(?m)^(LOPTS =.*)", "LOPTS = %s -pie" % get.LDFLAGS())

def build():
    shelltools.export("CC", get.CC())

    crosstools.make("libdir")
    crosstools.make()
    crosstools.make("ether-wake")
    crosstools.make("i18ndir")

def install():
    crosstools.rawInstall("BASEDIR=%s" % get.installDIR())

    pisitools.dosbin("ether-wake")
    pisitools.dosym("/bin/hostname", "/usr/bin/hostname")

    pisitools.dodoc("README", "README.ipv6", "TODO")
