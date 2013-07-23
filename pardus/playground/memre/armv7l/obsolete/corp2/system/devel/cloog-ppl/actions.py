#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import crosstools

WorkDir = "cloog-ppl"

def setup():
    crosstools.environment["LDFLAGS"] = "-Wl,-rpath,%(ToolchainDir)s/%(target)s/lib" % crosstools.environment

    crosstools.configure("--prefix=/usr \
                          --enable-shared \
                          --enable-static \
                          --with-gmp=%(RootDir)s/usr \
                          --with-ppl=%(RootDir)s/usr" %
                          crosstools.environment)

def build():
    crosstools.make()

def install():
    crosstools.install()
