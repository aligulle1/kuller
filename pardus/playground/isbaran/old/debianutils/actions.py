#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.configure()

def build():
    autotools.make()

def install():
    pisitools.dobin("tempfile", "/bin")
    pisitools.dobin("run-parts", "/bin")

    pisitools.doexe("savelog", "/usr/sbin")

    pisitools.dosbin("installkernel", "/sbin")
    pisitools.dosbin("mkboot")

    pisitools.doman("add-shell.8", "tempfile.1", "run-parts.8", "savelog.8", "installkernel.8", "mkboot.8")
    pisitools.dodoc("debian/changelog", "debian/control", "debian/copyright", "debian/README.shells")
