#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("Makefile", "CFLAGS += -g", "CFLAGS += -g " + get.CFLAGS())
    pisitools.dosed("Makefile", "(?m)^(CVSROOT =.*)")

def build():
    autotools.make()

def install():
    pisitools.dosbin("logrotate")
    pisitools.doman("logrotate.8")
    pisitools.dodoc("examples/logrotate*")

    pisitools.dodir("/etc/logrotate.d")
