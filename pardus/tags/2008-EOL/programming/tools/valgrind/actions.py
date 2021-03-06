#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("configure.in", 'CFLAGS="-Wno-long-long"', 'CFLAGS="%s -Wno-long-long"' % get.CFLAGS())
    pisitools.dosed("docs/Makefile.am", "doc/valgrind", "doc/%s" % get.srcTAG())

    autotools.autoreconf()
    autotools.configure("--with-x \
                         --without-mpicc")

def build():
    shelltools.cd("VEX/")
    shelltools.unlink("pub/libvex_guest_offsets.h")
    autotools.make("pub/libvex_guest_offsets.h")

    shelltools.cd("../")
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("ACKNOWLEDGEMENTS", "AUTHORS", "FAQ.txt", "NEWS", "README*")
