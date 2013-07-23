#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def define_global():
    shelltools.export("R_HOME_DIR", "/usr/lib/R")

def setup():
    define_global()
    autotools.configure("-enable-R-profiling \
                         --enable-R-shlib \
                         --enable-shared \
                         --enable-BLAS-shlib \
                         --with-blas \
                         --with-lapack \
                         --enable-mbcs \
                         --enable-utf8 \
                         --with-tcltk=no \
                         --with-system-pcre \
                         --with-system-zlib \
                         --with-x")

def build():
    define_global()
    autotools.make()

def install():
    define_global()
    autotools.install()
    pisitools.removeDir("/usr/bin")
    pisitools.dosym("/usr/lib/R/bin/R","/usr/bin/R")
