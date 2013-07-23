#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import crosstools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="xz-4.999.9beta"

def setup():
    crosstools.environment["CFLAGS"] = "%(CFLAGS)s -D_FILE_OFFSET_BITS=64" % crosstools.environment
    crosstools.environment["CXXFLAGS"] = "%(CXXFLAGS)s -D_FILE_OFFSET_BITS=64" % crosstools.environment

    crosstools.configure("--disable-static \
                          --disable-rpath \
                          --with-pic")

    # Remove RPATH
    pisitools.dosed("libtool", "^hardcode_libdir_flag_spec=.*", "hardcode_libdir_flag_spec=\"\"")
    pisitools.dosed("libtool", "^runpath_var=LD_RUN_PATH", "runpath_var=DIE_RPATH_DIE")

def build():
    crosstools.make()

def install():
    crosstools.install()

    for ext in ["", ".0", ".0.0.0"]:
        pisitools.dosym("liblzma.so.0.0.0", "/usr/lib/liblzmadec.so%s" % ext)

    pisitools.dosym("lzma.h", "/usr/include/lzmadec.h")
    pisitools.dosym("liblzma.pc", "/usr/lib/pkgconfig/liblzmadec.pc")

    pisitools.dodoc("AUTHORS","ChangeLog","COPYING*","NEWS","README")
