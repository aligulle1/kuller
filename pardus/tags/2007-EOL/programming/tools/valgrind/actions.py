#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005,2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("configure.in", "CFLAGS=\"-Wno-long-long\"", "CFLAGS=\"%s -Wno-long-long\"" % get.CFLAGS())
    # enlarges it from1GB - 128MB = 896MB and decreases the size of the kernel address space
    pisitools.dosed("configure.in", "valt_load_address_normal=\"0xb0000000\"", "valt_load_address_normal=\"0x30000000\"")
    pisitools.dosed("docs/Makefile.am", "doc/valgrind/", "doc/%s/" % get.srcTAG())

    autotools.autoconf()
    autotools.aclocal()
    autotools.automake()

    autotools.configure("--with-x \
                         --without-mpicc")

def build():
    shelltools.cd("VEX/")
    shelltools.unlink("pub/libvex_guest_offsets.h")
    autotools.make("pub/libvex_guest_offsets.h")
    shelltools.cd("../")
    autotools.make()

def install():
    pisitools.dodir("/usr/share/doc/valgrind-%s-%s/"% (get.srcVERSION(),get.srcRELEASE()))

    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("ACKNOWLEDGEMENTS", "AUTHORS", "FAQ.txt", "NEWS", "README*", "TODO")
