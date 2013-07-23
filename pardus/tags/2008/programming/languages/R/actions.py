#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    shelltools.export("R_HOME_DIR", "/usr/lib/R")
    shelltools.export("R_PDFVIEWER", "kpdf")
    shelltools.export("BLAS_LIBS","/usr/lib")

    autotools.aclocal("-I m4")
    autotools.autoconf()
    autotools.configure("--prefix=/usr \
                         --enable-R-profiling \
                         --enable-R-shlib \
                         --enable-shared \
                         --with-blas=-lblas \
                         --with-lapack \
                         --enable-mbcs \
                         --without-tcltk \
                         --with-readline \
                         --with-system-pcre \
                         --with-system-zlib \
                         --with-system-bzlib \
                         --with-x")

def build():
    autotools.make()

def check():
    autotools.make("check")

def install():
    autotools.install()

    pisitools.removeDir("/usr/bin")
    pisitools.dosym("/usr/lib/R/bin/R","/usr/bin/R")
    pisitools.dosym("/usr/lib/R/bin/Rscript","/usr/bin/Rscript")
