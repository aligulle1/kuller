#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def build():
    pisitools.dosed("Makefile", "-ltermcap", "-lncurses")
    autotools.make()

def install():
    pisitools.dobin("cdecl")
    pisitools.dosym("/usr/bin/cdecl","/usr/bin/c++decl")

    pisitools.doman("*.1")
    pisitools.dodoc("README")
