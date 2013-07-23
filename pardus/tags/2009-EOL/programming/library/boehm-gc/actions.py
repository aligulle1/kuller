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

WorkDir = "gc-%s" % get.srcVERSION()

def setup():
    shelltools.unlink("aclocal.m4")
    shelltools.unlink("libtool.m4")
    autotools.autoreconf("-fi")
    autotools.configure("--enable-cplusplus \
                         --disable-static")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.newman("doc/gc.man", "GC_malloc.1")
    pisitools.dohtml("doc")
    pisitools.dodoc("ChangeLog","doc/README","doc/README.changes")
