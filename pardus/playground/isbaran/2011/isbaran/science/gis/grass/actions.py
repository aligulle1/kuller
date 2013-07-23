#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("configure", "--libmysqld-libs", "--libs")
    # TODO add ffmpeg support
    autotools.configure("--with-cxx \
                         --enable-shared \
                         --disable-static \
                         --datadir=/usr/share/grass \
                         --with-curses \
                         --with-proj \
                         --with-proj-includes=/usr/include \
                         --with-proj-libs=/usr/lib \
                         --with-proj-share=/usr/share/proj \
                         --with-gdal \
                         --without-glw \
                         --with-postgres \
                         --with-sqlite \
                         --with-mysql \
                         --with-mysql-includes=/usr/include/mysql \
                         --with-opengl \
                         --enable-largefile \
                         --with-x \
                         --with-odbc \
                         --with-blas \
                         --with-lapack \
                         --with-fftw \
                         --with-cairo \
                         --with-python \
                         --with-freetype=yes \
                         --with-motif \
                         --without-ffmpeg \
                         --with-wxwidgets=wx-config \
                         --with-readline \
                         --with-readline-includes=/usr/include/readline \
                         --with-readline-libs=/lib \
                         --with-postgres-includes=/usr/include/postgresql \
                         --with-freetype-includes=/usr/include/freetype2")

def build():
    autotools.make("htmldocs-single")
    autotools.make()

def install():
    autotools.install()

    _inst = "/usr/grass-6.4.0/"
    for i in ["AUTHORS", "CHANGES", "COPYING", "GPL.TXT", "REQUIREMENTS.html"]:
        pisitools.remove("%s%s" % (_inst, i))
        pisitools.dodoc(i)

    pisitools.domove(_inst + "docs/*", "/usr/share/doc/grass/")

    for i in ["driver", "scripts", "tools", "fonts", "etc", "bwidget", "bin"]:
        pisitools.domove("%s%s" % (_inst, i), "/usr/share/grass/")

    pisitools.domove(_inst + "man", "/usr/share/man")
    pisitools.domove(_inst + "lib", "/usr")
    pisitools.domove(_inst + "include/grass", "/usr/include")

    pisitools.removeDir(_inst + "include")
    pisitools.removeDir(_inst + "docs")
    pisitools.removeDir(_inst)
