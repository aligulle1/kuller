#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "kdeartwork-%s" % get.srcVERSION().split("_")[0]
NoStrip = ["/usr/kde/4/share"]

def setup():
    cmaketools.configure("-DCMAKE_BUILD_TYPE=release",installPrefix="/usr/kde/4")

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
