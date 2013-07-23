#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005, 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import kde
from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools

WorkDir = "kxmame/trunk"

def setup():
    autotools.make("-f Makefile.cvs -j1")
    kde.configure()

def build():
    kde.make()

def install():
    kde.install()
