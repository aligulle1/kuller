#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt
#

from pisi.actionsapi import kde
from pisi.actionsapi import pisitools

WorkDir = "ktechlab-svn-latest"

def setup():
    kde.configure()

def build():
    pisitools.dosed("src/Makefile", "libtechmath.la", "libmath.la")
    kde.make()

def install():
    kde.install()

    pisitools.domo("po/ktechlab.po", "tr", "ktechlab.mo")
