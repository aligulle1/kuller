#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

WorkDir="ecl-0.9j"

def setup():
    autotools.configure("--with-system-gmp \
                         --enable-boehm=system \
                         --with-clx")

def build():
    autotools.make("-j1")

def install():
    autotools.install()

    # Remove empty directory
    pisitools.removeDir("/usr/include/ecl/gc")

    pisitools.dodoc("ANNOUNCEMENT","Copyright","README.1st")
