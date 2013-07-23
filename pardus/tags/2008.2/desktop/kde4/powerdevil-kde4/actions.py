#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import get

WorkDir = "powerdevil-%s-kde4.1.3" % get.srcVERSION()

def setup():
    cmaketools.configure("-DCMAKE_INSTALL_PREFIX=/usr/kde/4 \
                          -DDBUS_INTERFACES_INSTALL_DIR=/usr/kde/4/share/dbus-1/interfaces/")

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
