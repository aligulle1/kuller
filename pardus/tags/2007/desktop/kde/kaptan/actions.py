#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005,2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools

def setup():
    shelltools.system("cmake -DCMAKE_INSTALL_PREFIX=%s/usr/kde/3.5" % get.installDIR())

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.insinto("/usr/share/autostart","src/kaptan.desktop")
    pisitools.remove("/usr/kde/3.5/share/applications/kde/kaptan.desktop")
