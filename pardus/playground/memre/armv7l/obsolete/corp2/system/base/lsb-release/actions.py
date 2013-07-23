#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gp

from pisi.actionsapi import pisitools
from pisi.actionsapi import crosstools
from pisi.actionsapi import get

def build():
    pisitools.dosed("Makefile", "prefix=.*", "prefix=%s" % get.defaultprefixDIR())
    crosstools.make()

def install():
    crosstools.install()

    pisitools.dodir("/etc")

    pisitools.dodoc("README", "ChangeLog")
