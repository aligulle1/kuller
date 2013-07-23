#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import libtools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "unixODBC-2.2.11"

def setup():
    autotools.aclocal()
    libtools.libtoolize("-c -f")
    autotools.automake()
    autotools.autoconf()

def build():
    autotools.configure("--host=%s \
                         --prefix=/usr \
                         --sysconfdir=/etc/unixODBC \
                         --enable-gui=yes \
                         --x-libraries=/usr/lib" % (get.CHOST()))
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "NEWS", "README*")
    pisitools.dohtml("doc/*")
