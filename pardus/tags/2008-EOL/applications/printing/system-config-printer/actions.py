#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools

def setup():
    pisitools.dosed("Makefile.in", "xmlto man", "xmlto --skip-validation man")
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.install()

    # Remove GUI stuff
    pisitools.removeDir("/usr/bin")

    pisitools.dodoc("README", "AUTHORS", "NEWS", "COPYING", "ChangeLog")
