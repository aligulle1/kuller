#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def define_global():
    shelltools.export("R_HOME_DIR", "/usr/lib/R")
    shelltools.export("R_PDFVIEWER", "kpdf")

def setup():
    define_global()
    autotools.configure("--prefix=/usr \
                         --enable-R-profiling \
                         --enable-R-shlib \
                         --enable-shared \
                         --enable-BLAS-shlib \
                         --with-blas \
                         --with-lapack \
                         --enable-mbcs \
                         --enable-utf8 \
                         --without-tcltk \
                         --with-readline \
                         --with-system-pcre \
                         --with-system-zlib \
                         --with-system-bzlib \
                         --with-x")

def build():
    define_global()
    autotools.make()

def install():
    define_global()
    autotools.install()
    pisitools.removeDir("/usr/bin")
    pisitools.dosym("/usr/lib/R/bin/R","/usr/bin/R")
    pisitools.dosym("/usr/lib/R/bin/Rscript","/usr/bin/Rscript")
