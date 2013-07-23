#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "grass-6.4.0RC5"

def setup():
    autotools.configure("--with-cxx --enable-shared \
                         --disable-static --with-curses \
                         --with-proj --without-glw \
                         --with-postgres --with-sqlite \
                         --with-opengl --with-x \
                         --with-odbc --with-blas --with-lapack \
                         --with-cairo --with-freetype \
                         --with-motif \
                         --with-postgres-includes=/usr/include/postgresql \
                         --with-freetype-includes=/usr/include/freetype2")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
