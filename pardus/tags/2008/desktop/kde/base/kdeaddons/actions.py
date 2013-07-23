#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import kde
from pisi.actionsapi import shelltools

def setup():
    shelltools.export("DO_NOT_COMPILE", "atlantikdesigner noatun-plugins ksig")

    kde.configure("--with-sdl \
                   --without-xmms \
                   --with-berkeley-db")

def build():
    kde.make()

def install():
    kde.install()
