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

def setup():
    pisitools.dosed("PF_EXT_SLIB:=", "PF_EXT_SLIB:=stealth /g", "extensions/Makefile")

def build():
    autotools.make('COPT_FLAGS="%s -fPIC" \
                    CC="%s" \
                    KERNEL_DIR="/usr" \
                    PREFIX= \
                    LIBDIR="/usr/lib" \
                    BINDIR="/sbin" \
                    MANDIR="/usr/share/man" \
                    INCDIR="/usr/include" \
                    ' % (get.CFLAGS(), get.CC()))

def install():
    autotools.rawInstall('COPT_FLAGS="%s -fPIC" \
                          CC="%s" \
                          KERNEL_DIR="/usr" \
                          PREFIX= \
                          LIBDIR="/usr/lib" \
                          BINDIR="/sbin" \
                          MANDIR="/usr/share/man" \
                          INCDIR="/usr/include" \
                          DESTDIR="%s" \
                          ' % (get.CFLAGS(), get.CC(), get.installDIR()))

    autotools.make('LIBDIR="/usr/lib" \
                    INCDIR="/usr/include" \
                    DESTDIR="%s" \
                    MANDIR="/usr/share/man" \
                    install-devel' % get.installDIR())

    pisitools.dodir("/var/lib/iptables")
    pisitools.dodir("/etc/iptables")
