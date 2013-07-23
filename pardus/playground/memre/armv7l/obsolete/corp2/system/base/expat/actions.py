#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import crosstools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    crosstools.environment["CFLAGS"] = "%(CFLAGS)s -fPIC" % crosstools.environment
    crosstools.configure("--disable-static")

def build():
    crosstools.make("-j1")

def install():
    crosstools.install('man1dir="%s/usr/share/man/man1"' % get.installDIR())

    pisitools.dohtml("doc/*")
    pisitools.dodoc("Changes", "README")
