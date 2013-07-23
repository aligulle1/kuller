#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("doc/Makefile.in", "^htmldir.*$", "htmldir = ${datadir}/doc/%s/html" % get.srcTAG())
    pisitools.dosed("doc/Makefile.in", "^dvidir.*$", "dvidir = ${datadir}/doc/%s" % get.srcTAG())
    autotools.configure("--enable-static=no")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.removeDir("/usr/share/aclocal")
    pisitools.removeDir("/usr/share/man")
    pisitools.removeDir("/usr/bin")
