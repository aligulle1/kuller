#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import libtools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    autotools.aclocal()
    libtools.libtoolize("--copy --force")
    autotools.automake()
    autotools.autoconf()

    autotools.configure("--enable-shared \
                        --enable-part-static \
                        --enable-pc98=no \
                        --enable-Werror=no \
                        --disable-dynamic-loading")

def build():
    # -D_GNU_SOURCE Needed for O_DIRECT
    pisitools.dosed("libparted/Makefile", "DEFS = -DHAVE_CONFIG_H", "DEFS = -DHAVE_CONFIG_H -D_GNU_SOURCE")
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("AUTHORS", "BUGS", "ChangeLog", "INSTALL", "NEWS", "README", "THANKS", "TODO")
    pisitools.dodoc("doc/API", "doc/FAQ", "doc/FAT")
