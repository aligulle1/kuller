#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import crosstools as autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import libtools
from pisi.actionsapi import get

def setup():
    autotools.autoconf()
    autotools.environment["CXXFLAGS"] = "%(CXXFLAGS)s -lstdc++" % autotools.environment
    autotools.configure("--with-pic \
                         --with-gnu-ld \
                         --disable-rpath \
                         --enable-ogg \
                         --disable-thorough-tests \
                         --disable-oggtest \
                         --with-ogg-includes=%(SysRoot)s/usr/include \
                         --with-ogg-libraries=%(SysRoot)s/usr/lib \
                         --disable-id3libtest \
                         --disable-xmms-plugin \
                         --without-xmms-prefix \
                         --without-xmms-exec-prefix \
                         --without-libiconv-prefix \
                         --disable-doxygen-docs \
                         --disable-dependency-tracking \
                         --disable-static" % autotools.environment)
    pisitools.dosed("src/libFLAC/Makefile", "-Wl,-read_only_relocs,warning")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.removeDir("/usr/share/doc/")

    pisitools.dohtml("doc/html/*")
