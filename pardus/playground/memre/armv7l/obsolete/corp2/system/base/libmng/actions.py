#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import crosstools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.sym("makefiles/configure.in","configure.in")
    shelltools.sym("makefiles/Makefile.am","Makefile.am")

    crosstools.autoreconf("-fi")
    crosstools.configure("--with-jpeg \
                          --with-lcms \
                          --disable-static")

def build():
    crosstools.make()

def install():
    crosstools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dohtml("doc")
    pisitools.doman("doc/man/*")
    pisitools.dodoc("CHANGES", "LICENSE", "README", "doc/libmng.txt")
