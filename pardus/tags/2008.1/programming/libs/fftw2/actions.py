#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools

WorkDir="fftw-2.1.5"

def setup():
    autotools.configure("--enable-shared \
                         --enable-threads \
                         --enable-i386-hacks \
                         --disable-static")
def build():
    autotools.make()

def install():
    autotools.install()
