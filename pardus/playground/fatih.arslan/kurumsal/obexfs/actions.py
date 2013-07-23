#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2011 TUBITAK/BILGEM
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools

def setup():
    shelltools.export("OBEXFTP_CFLAGS", "-I/usr/include/obexftp -I/usr/include/multicobex -I/usr/include/bfb")
    shelltools.export("OBEXFTP_LIBS", "-lobexftp -lmulticobex -lbfb -lopenobex -lbluetooth")
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.install()

