#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.configure("--disable-static")

def build():
    autotools.make()

def install():
    autotools.install()

    #install HAL file for portable audio players
    pisitools.insinto("/usr/share/hal/fdi/information/20thirdparty", "libmtp.fdi", "10-libmtp.fdi")

    #install UDEV rules
    pisitools.insinto("/etc/udev/rules.d/", "libmtp.rules", "65-mtp.rules")

    pisitools.removeDir("/usr/share/doc")
    pisitools.dohtml("doc/html/*")
    pisitools.dodoc("ChangeLog", "COPYING", "README", "AUTHORS", "TODO")
