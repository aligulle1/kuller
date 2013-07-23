#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import kerneltools
from pisi.actionsapi import get

import os

WorkDir = "klibc-%s" % get.srcVERSION()
NoStrip = "/"
KDIR = kerneltools.getKernelVersion()

docs = {"usr/klibc/arch/README": "README.arch",
        "usr/dash/README.klibc": "README.dash",
        "usr/dash/TOUR": "TOUR.dash",
        "usr/gzip/README": "README.gzip",
        "usr/gzip/COPYING": "COPYING.gzip",
        "usr/kinit/README": "README.kinit"}

_build="i686-pc-linux-gnu"
_host="arm-cortex_a8-linux-gnueabi"
_target=_host

# ugly hard-coded stuff, unfortunately..
_RootDir="/pardus-arm"
_ToolchainDir = "/home/memre/x-tools"

# ulgiest code ever, but temporary.
_KernelVersion = "2.6.29-omap1"

# Pardus-ARM preparation
def prepare():
    shelltools.export("LC_ALL", "C")
    shelltools.export("CXXFLAGS", "-I%s/usr/include -L%s/usr/lib -L%s/lib" % (_RootDir, _RootDir, _RootDir))
    shelltools.export("CFLAGS",   "-I%s/usr/include -L%s/usr/lib -L%s/lib" % (_RootDir, _RootDir, _RootDir))
    shelltools.export("LDFLAGS",  "-L%s/usr/lib -L%s/lib" % (_RootDir, _RootDir))

    shelltools.export("CC",     "%s-gcc" % _target)
    shelltools.export("CXX",    "%s-g++" % _target)
    shelltools.export("AR",     "%s-ar"  % _target)
    shelltools.export("AS",     "%s-as"  % _target)
    shelltools.export("LD",     "%s-ld"  % _target)
    shelltools.export("RANLIB", "%s-ranlib"  % _target)
    shelltools.export("OBJDUMP","%s-objdump" % _target)
    shelltools.export("STRIP",  "%s-strip"   % _target)
    shelltools.export("LIBTOOL","%s-libtool" % _target)

def fixperms(d):
    for root, dirs, files in os.walk(d):
        for name in dirs:
            shelltools.chmod(os.path.join(root, name), 0755)
        for name in files:
            shelltools.chmod(os.path.join(root, name), 0644)

def setup():
    # Pardus-ARM preparation
    prepare()

    shelltools.sym("%s/lib/modules/%s/build" % (_RootDir, _KernelVersion), "linux")

    # set the build directory
    shelltools.echo("MCONFIG", "KRNLOBJ = /lib/modules/%s/build" % KDIR)

    # Workaround for prelink warnings
    shelltools.echo("70klibc", 'PRELINK_PATH_MASK="/usr/lib/klibc"')

    pisitools.dosed("Makefile", "/man", "/share/man")

def build():
    # Pardus-ARM preparation
    prepare()

    shelltools.export("ARCH", "")
    autotools.make('EXTRA_KLIBCAFLAGS="-Wa,--noexecstack" \
                    EXTRA_KLIBCLDFLAGS="-z,noexecstack" \
                    HOSTCC="%s-gcc"\
                    CROSS_COMPILE=%s \
                    ARCH=arm \
                    libdir=/usr/lib \
                    SHLIBDIR=/lib \
                    mandir=/usr/share/man \
                    INSTALLDIR=/usr/lib/klibc' % (_build, _host))

def install():
    shelltools.export("ARCH", "")
    autotools.rawInstall('EXTRA_KLIBCAFLAGS="-Wa,--noexecstack" \
                          EXTRA_KLIBCLDFLAGS="-z,noexecstack" \
                          HOSTCC="%s-gcc"\
                          CROSS_COMPILE=%s- \
                          ARCH=arm \
                          libdir=/usr/lib \
                          SHLIBDIR=/lib \
                          mandir=/usr/share/man \
                          INSTALLDIR=/usr/lib/klibc \
                          INSTALLROOT="%s" ' % (_build, _host, get.installDIR()))

    asmSrcDir = "linux/arch/arm/include/asm"
    asmTargetDir = "/usr/lib/klibc/include/asm"

    # just a workaround for installer bug with 2.6.24, will make it sane later
    pisitools.remove(asmTargetDir)
    pisitools.dosym("asm-arm", asmTargetDir)

    # yet another new kernel compatibility workaround for 2.6.28 and above
    for f in shelltools.ls(asmSrcDir):
        pisitools.insinto(asmTargetDir, "%s/%s" % (asmSrcDir, f))

    fixperms("%s/usr/lib/klibc/include" % get.installDIR())

    for f in ["gunzip", "zcat"]:
        pisitools.remove("/usr/lib/klibc/bin/%s" % f)
        pisitools.dosym("gzip", "/usr/lib/klibc/bin/%s" % f)

    pisitools.dodoc("README", "usr/klibc/LICENSE", "usr/klibc/CAVEATS")

    for f in docs:
        pisitools.newdoc(f, docs[f])

