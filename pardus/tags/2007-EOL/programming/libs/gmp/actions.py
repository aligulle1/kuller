#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005,2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.configure("--enable-cxx \
                         --enable-fat \
                         --disable-mpfr \
                         --disable-mpbsd \
                         --localstatedir=/var/state/gmp")

def build():
    autotools.make()
    autotools.make("check")
    autotools.make("pdf")

def install():
    autotools.install()

    pisitools.dodoc("doc/*.pdf")
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "COPYING.LIB", "NEWS", "README")
