#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

import os

WorkDir = "klibc-%s" % get.srcVERSION()
NoStrip = "/"

docs = {"usr/klibc/arch/README": "README.arch",
        "usr/dash/README.klibc": "README.dash",
        "usr/dash/TOUR": "TOUR.dash",
        "usr/gzip/README": "README.gzip",
        "usr/gzip/COPYING": "COPYING.gzip",
        "usr/kinit/README": "README.kinit"}

def fixperms(d):
    for root, dirs, files in os.walk(d):
        for name in dirs:
            shelltools.chmod(os.path.join(root, name), 0755)
        for name in files:
            shelltools.chmod(os.path.join(root, name), 0644)

def setup():
    shelltools.sym("/lib/modules/%s/source" % get.curKERNEL(), "linux")

    # set the build directory
    shelltools.echo("MCONFIG", "KRNLOBJ = /lib/modules/%s/source" % get.curKERNEL())

    # Workaround for prelink warnings
    shelltools.echo("70klibc", 'PRELINK_PATH_MASK="/usr/lib/klibc"')

    pisitools.dosed("Makefile", "/man", "/share/man")

def build():
    shelltools.export("ARCH", "")
    autotools.make('EXTRA_KLIBCAFLAGS="-Wa,--noexecstack" \
                    EXTRA_KLIBCLDFLAGS="-z,noexecstack" \
                    HOSTCC="%s" CC="%s" \
                    KLIBCARCH=i386 \
                    KLIBCASMARCH=x86 \
                    libdir=/usr/lib \
                    SHLIBDIR=/lib \
                    mandir=/usr/share/man \
                    INSTALLDIR=/usr/lib/klibc' % (get.CC(), get.CC()))

def install():
    shelltools.export("ARCH", "")
    autotools.rawInstall('EXTRA_KLIBCAFLAGS="-Wa,--noexecstack" \
                          EXTRA_KLIBCLDFLAGS="-z,noexecstack" \
                          HOSTCC="%s" CC="%s" \
                          KLIBCARCH=i386 \
                          KLIBCASMARCH=x86 \
                          libdir=/usr/lib \
                          SHLIBDIR=/lib \
                          mandir=/usr/share/man \
                          INSTALLROOT="%s" \
                          INSTALLDIR=/usr/lib/klibc' % (get.CC(), get.CC(), get.installDIR()))

    # just a workaround for installer bug with 2.6.24, will make it sane later
    pisitools.remove("/usr/lib/klibc/include/asm")
    pisitools.dosym("asm-x86", "/usr/lib/klibc/include/asm")

    fixperms("%s/usr/lib/klibc/include" % get.installDIR())

    for f in ["gunzip", "zcat"]:
        pisitools.remove("/usr/lib/klibc/bin/%s" % f)
        pisitools.dosym("gzip", "/usr/lib/klibc/bin/%s" % f)

    pisitools.dodoc("README", "klibc/LICENSE", "klibc/CAVEATS")

    for f in docs:
        pisitools.newdoc(f, docs[f])

