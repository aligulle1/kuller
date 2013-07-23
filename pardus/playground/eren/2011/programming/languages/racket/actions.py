#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2011 TUBITAK/BILGEM
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

WorkDir="racket-%s/src" % get.srcVERSION()

def setup():
    # remove built-in libffi library
    # pisitools.removeDir("foreign/libffi")

    autotools.configure("--enable-shared \
                         --enable-gracket \
                         --enable-plot \
                         --enable-docs \
                         --enable-jit \
                         --enable-places \
                         --enable-backtrace \
                         --enable-pthread \
                         --disable-perl")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

