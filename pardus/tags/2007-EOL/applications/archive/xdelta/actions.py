#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005,2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import libtools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    shelltools.export("WANT_AUTOCONF", "2.5")

    libtools.libtoolize("--copy --force")
    autotools.aclocal()
    autotools.automake("--add-missing")
    autotools.autoheader()
    autotools.autoconf()

    autotools.configure()

def build():
    autotools.make("CFLAGS=\"%s -I/usr/include/glib-2.0 -I/usr/lib/glib-2.0/include\"" % get.CFLAGS())

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.remove("/usr/lib/*.a")
