#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def build():
    pisitools.dosed("utils/Makefile", "\(PREFIX\)/man", "(PREFIX)/share/man")
    for e in ("Makefile", "utils/Makefile"):
        pisitools.dosed(e, "/usr/local", "usr")
        pisitools.dosed(e, "\(PREFIX\)/bin", "(PREFIX)/sbin")
        pisitools.dosed(e, "CFLAGS = -g -O2", "CFLAGS = %s" % get.CFLAGS())

    autotools.make()
    shelltools.cd("utils")
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    shelltools.cd("utils")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    shelltools.cd("..")
    pisitools.dodoc("examples/*.txt", "CHANGELOG", "COVERAGE", "CREDITS", "README*")
    pisitools.dohtml("doc/*html")
