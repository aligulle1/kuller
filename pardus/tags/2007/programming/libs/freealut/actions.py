#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005, 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import libtools
from pisi.actionsapi import get

def setup():
    shelltools.export("AT_M4DIR", "admin/autotools/m4")
    autotools.autoreconf()
    libtools.libtoolize("--copy --force")

    autotools.configure("--libdir=/usr/lib\
                         --disable-static")

def build():
    autotools.make("all")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR()) 
    pisitools.dodoc("AUTHORS", "ChangeLog", "NEWS", "README")
    pisitools.dohtml("doc/*")

