#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import libtools
from pisi.actionsapi import get

WorkDir = "libnet"

def setup():
    libtools.libtoolize("--force")
    autotools.aclocal()
    autotools.automake("--add-missing --copy")
    autotools.autoconf()

    autotools.configure("--disable-static \
                         --with-pf_packet=yes")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.doman("doc/man/man3/*.3")
    pisitools.dohtml("doc/html/*")
    pisitools.dodoc("VERSION", "README", "doc/CHANGELOG")
