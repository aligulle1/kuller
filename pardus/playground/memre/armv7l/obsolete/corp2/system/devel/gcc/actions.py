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

def setup():
    shelltools.makedirs("build")
    shelltools.cd("build")

    crosstools.environment["LDFLAGS"] = "-Wl,-rpath,%(ToolchainDir)s/%(target)s/lib \
                                           -I%(RootDir)s/usr/include \
                                           -L%(RootDir)s/usr/lib \
                                           -L%(RootDir)s/lib" % crosstools.environment
    crosstools.prepare()

    shelltools.system('../configure \
                       --build=%(build)s --host=%(host)s --target=%(target)s \
                       --prefix=/usr \
                       --bindir=/usr/bin \
                       --libdir=/usr/lib \
                       --libexecdir=/usr/lib \
                       --includedir=/usr/include \
                       --mandir=/usr/share/man \
                       --infodir=/usr/share/info \
                       --with-gxx-include-dir=/usr/include/c++ \
                       --disable-libgcj \
                       --disable-multilib \
                       --disable-nls \
                       --disable-mudflap \
                       --disable-libmudflap \
                       --enable-checking=release \
                       --enable-clocale=gnu \
                       --enable-__cxa_atexit \
                       --enable-languages=c,c++ \
                       --enable-libstdcxx-allocator=new \
                       --disable-libstdcxx-pch \
                       --enable-shared \
                       --enable-ssp \
                       --enable-libssp \
                       --disable-bootstrap \
                       --disable-libgomp \
                       --disable-libmudflap \
                       --enable-threads=posix \
                       --without-included-gettext \
                       --without-system-libunwind \
                       --with-system-zlib \
                       --with-pkgversion="Pardus Linux for ARM" \
                       --with-bugurl=http://bugs.pardus.org.tr' %
                       crosstools.environment)

    shelltools.system("cp Makefile{,.orig}; \
                       sed \"/^HOST_\(GMP\|PPL\|CLOOG\)\(LIBS\|INC\)/s:-[IL]/\(lib\|include\)::\" \
                       Makefile.orig > Makefile")

def build():
    shelltools.cd("build")
    #crosstools.make('BOOT_CFLAGS="%s" profiledbootstrap' % get.CFLAGS())
    crosstools.make()

def install():
    shelltools.cd("build")
    crosstools.rawInstall("DESTDIR=%s" % get.installDIR())

    for header in ["limits.h","syslimits.h"]:
        pisitools.insinto("/usr/lib/gcc/%s/4.4.3/include" % get.HOST() , "gcc/include-fixed/%s" % header)

    # Not needed
    pisitools.removeDir("/usr/lib/gcc/*/*/include-fixed")
    pisitools.removeDir("/usr/lib/gcc/*/*/install-tools")

    # This one comes with binutils
    pisitools.remove("/usr/lib/libiberty.a")

    # cc symlink
    pisitools.dosym("../usr/bin/gcc" , "/bin/cc")

    # /lib/cpp symlink for legacy X11 stuff
    pisitools.dosym("../usr/bin/cpp", "/lib/cpp")

