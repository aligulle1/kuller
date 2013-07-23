#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    autotools.make()

def install():
    pisitools.dodir("/usr/lib")
    pisitools.dodir("/usr/include")
    pisitools.insinto("/usr/lib", "src/libaio.a")
    pisitools.insinto("/usr/include","src/libaio.h")
    pisitools.insinto("/usr/lib", "src/libaio.so.1.0.1")
    pisitools.dosym("/usr/lib/libaio.so.1.0.1", "/usr/lib/libaio.so")
    pisitools.dosym("/usr/lib/libaio.so.1.0.1", "/usr/lib/libaio.so.1")
    pisitools.dodoc("ChangeLog", "COPYING", "TODO")
