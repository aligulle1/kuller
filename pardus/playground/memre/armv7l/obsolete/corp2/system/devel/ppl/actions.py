#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import crosstools

def setup():
    crosstools.environment["CPPFLAGS"] = "-fexceptions"

    crosstools.configure("--prefix=/usr \
                          --with-libgmp-prefix=%(RootDir)s/usr \
                          --with-libgmpxx-prefix=%(RootDir)s/usr \
                          --enable-shared \
                          --enable-static \
                          --disable-optimization \
                          --enable-check=quick" %
                          crosstools.environment)

def build():
    crosstools.make()

def install():
    crosstools.install()
