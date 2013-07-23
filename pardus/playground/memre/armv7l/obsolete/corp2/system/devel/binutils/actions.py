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
    crosstools.prepare()

    # Build binutils with LD_SYMBOLIC_FUNCTIONS=1 and reduce PLT relocations in libfd.so by 84%.
    shelltools.export("LD_SYMBOLIC_FUNCTIONS", "1")

    shelltools.system('AR=ar AS=as ./configure \
                       --prefix=/%(defaultprefixDIR)s \
                       --mandir=/%(manDIR)s \
                       --infodir=/%(infoDIR)s \
                       --datadir=/%(dataDIR)s \
                       --sysconfdir=/%(sysconfDIR)s \
                       --localstatedir=/%(localstateDIR)s \
                       --libexecdir=/%(libexecDIR)s \
                       --build=%(build)s \
                       --host=%(host)s \
                       --target=%(target)s \
                       --disable-nls \
                       --disable-werror \
                       --enable-shared \
                       --with-pkgversion="Pardus Linux for ARM" \
                       --with-bugurl=http://bugs.pardus.org.tr/' %
                       crosstools.environment)

    crosstools.make("configure-host")

def build():
    crosstools.make("-j1 all")
    crosstools.make("-j1 info")

def install():
    crosstools.rawInstall("DESTDIR=%s tooldir=/usr" % get.installDIR())

    # Rebuild libbfd.a and libiberty.a with -fPIC
    pisitools.remove("/usr/lib/libbfd.a")
    pisitools.remove("/usr/lib/libiberty.a")
    #pisitools.remove("/usr/include/libiberty.h")

    crosstools.make("-C libiberty clean")
    crosstools.make('CFLAGS="-fPIC %s" -C libiberty' % get.CFLAGS())

    crosstools.make("-C bfd clean")
    crosstools.make('CFLAGS="-fPIC %s" -C bfd' % get.CFLAGS())

    pisitools.insinto("/usr/lib", "bfd/libbfd.a")
    pisitools.insinto("/usr/lib", "libiberty/libiberty.a")
    pisitools.insinto("/usr/include", "include/libiberty.h")

    # Prevent programs to link against libbfd and libopcodes dynamically,
    # they are changing far too often
    pisitools.remove("/usr/lib/libopcodes.so")
    pisitools.remove("/usr/lib/libbfd.so")

    # Remove libtool files, which reference the .so libs
    pisitools.remove("/usr/lib/libopcodes.la")
    pisitools.remove("/usr/lib/libbfd.la")
