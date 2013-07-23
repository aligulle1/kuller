#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "linux-2.6.15"

def build():
    shelltools.touch("include/linux/autoconf.h")
    shelltools.sym("asm-i386", "include/asm")

    shelltools.export("HOSTCFLAGS", "-Wall -Wstrict-prototypes -O2 -fomit-frame-pointer -Iinclude/")
    shelltools.export("MOPT", "ARCH=i386 CROSS_COMPILE=i686-pc-linux-gnu-")
                      
    autotools.make("defconfig HOSTCFLAGS=\"${HOSTCFLAGS}\" ${MOPT}")
    
    autotools.make("prepare HOSTCFLAGS=\"${HOSTCFLAGS}\" ${MOPT}")
    autotools.make("prepare-all HOSTCFLAGS=\"${HOSTCFLAGS}\" ${MOPT}")

def install():
    pisitools.dodir("/usr/include/")

    shelltools.copytree("include/linux/", "%s/usr/include/linux/" % get.installDIR())
    shelltools.copytree("include/asm/", "%s/usr/include/asm/" % get.installDIR())
    shelltools.copytree("include/asm-generic/", "%s/usr/include/asm-generic/" % get.installDIR())
