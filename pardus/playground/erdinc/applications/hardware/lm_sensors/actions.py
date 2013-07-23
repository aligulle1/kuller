#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    shelltools.export("CC", get.CC())
    autotools.make()

def install():
    autotools.make("DESTDIR=%s \
                    PREFIX=/usr \
                    MANDIR=/usr/share/man \
                    LIBDIR=/usr/lib install" % get.installDIR())

    pisitools.dodoc("CHANGES", "CONTRIBUTORS", "README")
    pisitools.dohtml("doc/lm_sensors-FAQ.html")
    pisitools.insinto("/usr/share/doc/%s/doc" % get.srcTAG(), "doc/chips")
    pisitools.insinto("/usr/share/doc/%s/doc/developers" % get.srcTAG(), "doc/developers/*")
