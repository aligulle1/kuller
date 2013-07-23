#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.export("MONO_SHARED_DIR", get.workDIR())

    autotools.configure("--disable-static")

def build():
    shelltools.export("MONO_SHARED_DIR", get.workDIR())

    # u really suck
    shelltools.export("LC_ALL", "C")
    autotools.make()

def install():
    shelltools.export("MONO_SHARED_DIR", get.workDIR())

    autotools.install()

    pisitools.dodoc("ChangeLog", "README*")
