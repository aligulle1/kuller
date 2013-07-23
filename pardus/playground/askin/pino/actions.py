#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import shelltools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import get

WorkDir="pino-0.2.10"

def setup():
    shelltools.makedirs("build")
    shelltools.cd("build")
    cmaketools.configure("DCMAKE_INSTALL_PREFIX=/usr -DUBUNTU_ICONS=OFF -DENABLE_DEBUG=OFF", sourceDir = "..")

def build():
    shelltools.cd("build")
    cmaketools.make()

def install():
    shelltools.cd("build")
    cmaketools.install()
