#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("Makefile", "Class\-Path\:\ \$\(JARDIR\)\/hexdump.jar", "Class-Path: hexdump.jar")
    pisitools.dosed("Makefile", "JCFLAGS\+\=.*", "JCFLAGS+=")

def build():
    autotools.make("-j1")

def install():
    autotools.install("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("changelog", "COPYING", "README")

