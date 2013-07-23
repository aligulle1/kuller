#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005,2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.system("cmake -DCMAKE_INSTALL_PREFIX=%s/%s" % (get.installDIR(),get.kdeDIR()))

def build():
    autotools.make()

def install():
    autotools.install()
