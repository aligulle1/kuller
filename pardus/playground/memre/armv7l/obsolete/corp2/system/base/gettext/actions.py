#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import crosstools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

docdir = "/%s/%s" % (get.docDIR(), get.srcNAME())

def setup():
    cache = [ "am_cv_func_iconv_works=yes",
              "gl_cv_func_wcwidth_works=yes",
              "gt_cv_func_printf_posix=yes",
              "gt_cv_int_divbyzero_sigfpe=yes" ]

    # FIXME: optimization flags
    crosstools.environment["CFLAGS"] = "-O3 -march=armv7-a -mtune=cortex-a8 -mfpu=neon -mfpu=vfp -mfloat-abi=softfp -I%(SysRoot)s/usr/include" % crosstools.environment
    crosstools.environment["CXXFLAGS"] = "-O3 -march=armv7-a -mtune=cortex-a8 -mfpu=neon -mfpu=vfp -mfloat-abi=softfp -I%(SysRoot)s/usr/include" % crosstools.environment

    #crosstools.environment["CFLAGS"] = "%(CFLAGS)s -Dgcc_is_lint" % crosstools.environment
    #crosstools.environment["CXXFLAGS"] = "%(CXXFLAGS)s -Dgcc_is_lint" % crosstools.environment

    # Build with --without-included-gettext (will use that of glibc), as we
    # need preloadable_libintl.so for new help2man
    crosstools.autoreconf("-fiv")
    crosstools.configure("--disable-java \
                          --disable-csharp \
                          --without-included-gettext \
                          --with-included-libcroco \
                          --with-included-glib \
                          --with-included-libxml \
                          --without-emacs \
                          --disable-openmp \
                          --enable-nls \
                          --enable-shared \
                          --disable-rpath \
                          --disable-static", cache=cache)

def build():
    crosstools.make("GMSGFMT=../src/msgfmt")

def install():
    crosstools.rawInstall("DESTDIR=%s docdir=/%s/html" % (get.installDIR(), docdir))

    pisitools.doexe("gettext-tools/misc/gettextize", "/usr/bin")

    # Remove C# & Java stuff
    pisitools.remove("%s/html/examples/build-aux/csharp*" % docdir)
    pisitools.remove("%s/html/examples/build-aux/java*" % docdir)
    pisitools.removeDir("%s/html/examples/*java*" % docdir)
    pisitools.removeDir("%s/html/*java*" % docdir)

    pisitools.dodoc("AUTHORS", "COPYING", "ChangeLog*", "HACKING", "NEWS", "README*", "THANKS")
