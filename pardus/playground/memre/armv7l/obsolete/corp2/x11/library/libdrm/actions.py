#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import crosstools as autotools

def setup():
    autotools.autoreconf("-vif")
    autotools.configure("--enable-udev \
                         --disable-intel \
                         --enable-nouveau-experimental-api")

def build():
    autotools.make()

def install():
    autotools.install()
