#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "FlightGear-%s" % get.srcVERSION()

def setup():
    autotools.configure("--with-multiplayer \
                         --with-network-olk \
                         --enable-sp-fdms \
                         --with-threads \
                         --with-x")

def build():
    autotools.make("-j1")

def install():
    autotools.install()
    pisitools.dodoc("README*", "ChangeLog", "AUTHORS", "NEWS", "Thanks")
