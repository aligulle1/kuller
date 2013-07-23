#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    autotools.make()

def install():
    pisitools.insinto("/usr/lib", "src/libaio.so.1.0.1")
    pisitools.dosym("/usr/lib/libaio.so.1.0.1", "/usr/lib/libaio.so")
    pisitools.dosym("/usr/lib/libaio.so.1.0.1", "/usr/lib/libaio.so.1")

    pisitools.insinto("/usr/include","src/libaio.h")

    pisitools.dodoc("ChangeLog", "COPYING", "TODO")
