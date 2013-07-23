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

WorkDir = "jpeg-6b"

def setup():
    shelltools.unlink("config.guess")
    shelltools.unlink("config.sub")
    shelltools.unlink("ltmain.sh")
    shelltools.unlink("ltconfig")

    shelltools.copy("/usr/share/aclocal/libtool.m4", "aclocal.m4")
    shelltools.system("cat /usr/share/aclocal/ltoptions.m4 \
                           /usr/share/aclocal/ltversion.m4 \
                           /usr/share/aclocal/ltsugar.m4 \
                           /usr/share/aclocal/lt~obsolete.m4 \
                           >>./aclocal.m4")

    libtools.libtoolize("--install")
    libtools.libtoolize()

    autotools.autoconf()

    options = "--enable-shared \
               --disable-static"

    if get.buildTYPE() == "emul32":
        # options += " --prefix=/emul32 --libdir=/usr/lib32"
        shelltools.export("CC", "%s -m32" % get.CC())
        shelltools.export("CXX", "%s -m32" % get.CC())
        shelltools.export("CFLAGS", "%s -m32" % get.CFLAGS())
        shelltools.export("CXXFLAGS", "%s -m32" % get.CFLAGS())
        shelltools.export("LDFLAGS", "%s -m32" % get.LDFLAGS())

    autotools.configure(options)

def build():
    autotools.make("-j1")

def install():
    # autotools.rawInstall('DESTDIR="%s"' % get.installDIR())
    if get.buildTYPE() != "emul32":
        pisitools.dolib_so(".libs/libjpeg.so.62.0.0")
        pisitools.dosym("/usr/lib/libjpeg.so.62.0.0", "/usr/lib/libjpeg.so.62")

    if get.buildTYPE() == "emul32":
        pisitools.dolib_so(".libs/libjpeg.so.62.0.0", "/usr/lib32")
        pisitools.dosym("/usr/lib32/libjpeg.so.62.0.0", "/usr/lib32/libjpeg.so.62")

    # if get.buildTYPE() == "emul32":
    #     pisitools.removeDir("/emul32")
    #    return

    # they say some programs use this
    # pisitools.insinto("/usr/include", "jpegint.h")
    # pisitools.insinto("/usr/include", "jinclude.h")

    pisitools.dodoc("change.log", "example.c", "README")
