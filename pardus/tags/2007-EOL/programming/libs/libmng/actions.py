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
    shelltools.sym("makefiles/configure.in","configure.in")
    shelltools.sym("makefiles/Makefile.am","Makefile.am")

    autotools.autoreconf("-fi")
    autotools.configure("--with-jpeg \
                         --with-lcms \
                         --disable-static")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("Changes", "LICENSE", "README*", "doc/doc.readme", "doc/libmng.txt")

    pisitools.doman("doc/man/*")
    pisitools.dohtml("doc")
