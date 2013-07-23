#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="STLport-%s" % get.srcVERSION()

def setup():
    pisitools.dosed("build/Makefiles/gmake/gcc.mak","OPT \+= -O2","OPT +=")
    pisitools.dosed("stlport/stl/_cwchar.h","_STLP_VENDOR_CSTD::wcsftime","::wcsftime")

    pisitools.echo("stlport/stl/config/user_config.h","#define _STLP_NATIVE_INCLUDE_PATH ../g++-v3/")

    pisitools.dosed("build/Makefiles/gmake/gcc.mak","^CFLAGS =.*","CFLAGS = %s" % get.CFLAGS())
    pisitools.dosed("build/Makefiles/gmake/gcc.mak","^CCFLAGS =.*","CCFLAGS = %s" % get.CFLAGS())

    shelltools.cd("build/lib")
    autotools.configure("--with-extra-cxxflags=\"%s\"" % get.CXXFLAGS())
    shelltools.cd("../..")

    pisitools.echo("build/Makefiles/config.mak","CFLAGS := %s" % get.CFLAGS())

def build():
    autotools.make("-j1 \
                    -C build/lib \
                    -f gcc.mak \
                    release-shared")

def install():
    autotools.make("-C build/lib -f gcc.mak install-release-shared \
                    INSTALL_BIN_DIR=%s/usr/bin INSTALL_LIB_DIR=%s/usr/lib" % (get.installDIR(),get.installDIR()))
    pisitools.insinto("/usr/include","stlport")

    pisitools.dodoc("README","etc/ChangeLog*")
