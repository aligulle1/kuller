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

def setup():
    autotools.configure("--disable-static")

    shelltools.copytree(".","mpfr-sse2")
    shelltools.cd("mpfr-sse2")
    shelltools.export("CFLAGS","%s -mtune=pentium4 -march=pentium4 -mcpu=pentium4" % get.CFLAGS())
    autotools.configure("--disable-static \
                         --host=pentium4-pc-linux")


def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.insinto("/usr/lib/sse2","mpfr-sse2/.libs/libmpfr.so.1.1.0")
    pisitools.dosym("/usr/lib/sse2/libmpfr.so.1.1.0","/usr/lib/sse2/libmpfr.so.1")

    pisitools.dohtml("FAQ.html")
    pisitools.dodoc("NEWS", "README", "TODO")

def check():
    autotools.make("check")
    shelltools.cd("mpfr-sse2")
    autotools.make("check")
