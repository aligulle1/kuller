#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import libtools
from pisi.actionsapi import get

WorkDir = "libmikmod-3.1.12"

def setup():
    shelltools.export("AT_M4DIR", "%s/m4" % get.curDIR())

    libtools.gnuconfig_update()

    options = "--disable-esd \
               --disable-af \
               --enable-alsa \
               --enable-oss \
               --disable-static"

    if get.buildTYPE() == "emul32":
        options += " --prefix=/emul32 \
                     --libdir=/usr/lib32 \
                     --bindir=/emul32/bin"

        shelltools.export("CC", "%s -m32" % get.CC())
        shelltools.export("CXX", "%s -m32" % get.CXX())
        shelltools.export("CFLAGS", "%s -m32" % get.CFLAGS())
        shelltools.export("CXXFLAGS", "%s -m32" % get.CFLAGS())
        shelltools.export("LDFLAGS", "%s -m32" % get.LDFLAGS())

    autotools.configure(options)

def build():
    autotools.make()

def install():
    if get.buildTYPE() != "emul32":
        pisitools.dolib_so("libmikmod/.libs/libmikmod.so.2.0.4")
        pisitools.dosym("/usr/lib/libmikmod.so.2.0.4", "/usr/lib/libmikmod.so.2")

    if get.buildTYPE() == "emul32":
        pisitools.dolib_so("libmikmod/.libs/libmikmod.so.2.0.4", "/usr/lib32")
        pisitools.dosym("/usr/lib32/libmikmod.so.2.0.4", "/usr/lib32/libmikmod.so.2")

    # pisitools.dodoc("AUTHORS", "NEWS", "README", "TODO")
    # pisitools.dohtml("docs/*.html")
