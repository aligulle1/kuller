#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006,2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import libtools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "."
SkipList = (".", "patches", "pisiBuildState")

def setup():
    # Speed up xkbcomp
    shelltools.export("CFLAGS","%s -DHAVE_STRCASECMP" % get.CFLAGS())

    for package in shelltools.ls("."):
        if package.startswith(SkipList):
            continue

        print "Configuring %s..." % package
        shelltools.cd(package)

        if package.startswith("xdm"):
            libtools.libtoolize("--copy --force")

        autotools.autoreconf("--install")
        autotools.configure("--disable-static")
        shelltools.cd("../")

def build():
    for package in shelltools.ls("."):
        if package.startswith(SkipList):
            continue

        shelltools.cd(package)
        autotools.make()
        shelltools.cd("../")

def install():
    for package in shelltools.ls("."):
        if package.startswith(SkipList):
            continue

        shelltools.cd(package)
        autotools.rawInstall("DESTDIR=%s" % get.installDIR())
        shelltools.cd("../")
