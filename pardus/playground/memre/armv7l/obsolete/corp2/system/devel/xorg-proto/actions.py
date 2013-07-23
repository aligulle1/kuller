#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import crosstools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "."
SkipFiles = [".pc", "filelist", "patches", "pisiBuildState"]

def setup():
    pisitools.dosed("*/Makefile.am", r"/doc/\$\(PACKAGE\)", "/doc/xorg-proto")

    for package in shelltools.ls("."):
        if package in SkipFiles:
            continue
        shelltools.cd(package)
        crosstools.autoreconf("-vif")
        crosstools.configure()
        shelltools.cd("../")

def build():
    for package in shelltools.ls("."):
        if package in SkipFiles:
            continue
        shelltools.cd(package)
        crosstools.make()
        shelltools.cd("../")

def install():
    for package in shelltools.ls("."):
        if package in SkipFiles:
            continue
        shelltools.cd(package)
        crosstools.rawInstall("DESTDIR=%s" % get.installDIR())
        shelltools.cd("../")
