#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "js/src"

def build():
    autotools.make("-j1 -f Makefile.ref JS_THREADSAFE=1")

def install():
    # make is picky about the order of install
    autotools.make("-f Makefile.ref install DESTDIR=%s" % (get.installDIR()))

    pisitools.remove("/usr/lib/libjs.a")

    pisitools.dodoc("../jsd/README")
    pisitools.dohtml("README.html")
