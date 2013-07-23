#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010-2011 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

NoStrip = ["/"]

WorkDir = "akiaLinuxPaketv%s" % get.srcVERSION()

def install():
    pisitools.insinto("/usr/share/applications", "akia.desktop")
    pisitools.insinto("/usr/share/pixmaps", "akia.png")
    pisitools.insinto("/usr/share/akia", "akia.jar")
    pisitools.insinto("/etc/akis", "akia.conf")

    pisitools.dolib_so("libakisp11.so")

    # Install libpkcs11wrapper.so for E-devlet
    pisitools.insinto("/usr/lib", "libpkcs11wrapper/libpkcs11wrapper.so.%s" % get.ARCH(), "libpkcs11wrapper.so")

    # FIXME: Application's fault, should write its log into $HOME
    pisitools.dodir("/var/log/akis")
    shelltools.chmod("%s/var/log/akis" % get.installDIR(), 0777)

    # FIXME: Application's fault, should read/write its configuration from $HOME
    shelltools.chmod("%s/etc/akis" % get.installDIR(), 0777)
