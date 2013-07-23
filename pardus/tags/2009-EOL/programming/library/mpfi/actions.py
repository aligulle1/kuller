#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure()

def build():
    autotools.make("-j1")

def check():
    shelltools.system("tests/test_mpfi")
    shelltools.system("tests/test_trigo")

def install():
    autotools.install()

    # Remove the static lib here
    pisitools.remove("/usr/lib/*.a")

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README")
