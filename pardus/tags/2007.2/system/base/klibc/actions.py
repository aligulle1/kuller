#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005, 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "klibc-%s" % get.srcVERSION()
NoStrip = "/"

def setup():
    # ugly workaround assuming kernel source is in /usr/src/linux
    shelltools.sym("/usr/src/linux", "linux")

    # set the build directory
    shelltools.echo("MCONFIG", "KRNLOBJ = /usr/src/linux")

    # Workaround for prelink warnings
    shelltools.echo("70klibc", 'PRELINK_PATH_MASK="/usr/lib/klibc"')

    pisitools.dosed("Makefile", "/man", "/share/man")

def build():
    shelltools.export("ARCH", "")
    autotools.make('EXTRA_KLIBCAFLAGS="-Wa,--noexecstack" \
                    EXTRA_KLIBCLDFLAGS="-z,noexecstack" \
                    libdir=/usr/lib \
                    SHLIBDIR=/lib \
                    mandir=/usr/share/man \
                    INSTALLDIR=/usr/lib/klibc')

def install():
    shelltools.export("ARCH", "")
    autotools.rawInstall('INSTALLROOT="%s"' % get.installDIR())

    pisitools.remove("/usr/lib/klibc/bin/gunzip")
    pisitools.remove("/usr/lib/klibc/bin/zcat")
    pisitools.dosym("gzip", "/usr/lib/klibc/bin/gunzip")
    pisitools.dosym("gzip", "/usr/lib/klibc/bin/zcat")

    pisitools.dodoc("README", "klibc/LICENSE", "klibc/CAVEATS")
    pisitools.newdoc("klibc/README", "README.klibc")
    pisitools.newdoc("klibc/arch/README", "README.klibc.arch")

    pisitools.newdoc("ash/README.klibc", "ash/README")
    pisitools.newdoc("gzip/README", "gzip/README")
    pisitools.newdoc("gzip/COPYING", "gzip/COPYING")
    pisitools.newdoc("ipconfig/README", "ipconfig/README")
    pisitools.newdoc("kinit/README", "kinit/README")

