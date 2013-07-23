#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import crosstools as autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.environment["CFLAGS"] = "%(CFLAGS)s -D__SOFTFP__" % autotools.environment
    autotools.autoconf()
    pisitools.dosed("man/Makefile.in", r"(^program_transform_name\s*=).*", "\\1")
    autotools.configure("--disable-static \
                         --with-gnu-ld \
                         --enable-shared \
                         --enable-target-optspace \
                         --enable-languages=c,c++,f77 \
                         --enable-threads=posix \
                         --enable-multilib \
                         --enable-c99 \
                         --enable-long-long \
                         --enable-symvers=gnu \
                         --enable-__cxa_atexit")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("ChangeLog*", "LICENSE", "README*", "TODO")
