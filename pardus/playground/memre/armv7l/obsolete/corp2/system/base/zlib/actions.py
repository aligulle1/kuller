#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import crosstools
from pisi.actionsapi import pisitools
from pisi.actionsapi import libtools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

version = get.srcVERSION()

def setup():
    crosstools.prepare()

    pisitools.dosed("Makefile*", "ldconfig \|\| ", "")

    # because of configure script is not built by autotools,
    # parameters of crosstools.configure method are not suitable
    shelltools.system("./configure \
                       --shared \
                       --prefix=/usr \
                       --libdir=/lib")

def build():
    crosstools.make()

def install():
    crosstools.install("libdir=%s/lib" % get.installDIR())
    pisitools.dolib("libz.so.%s" % version)

    shelltools.chmod("%s/lib/libz.so.*" % get.installDIR())
    libtools.gen_usr_ldscript("libz.so")

    pisitools.remove("/lib/libz.a")

    for header in ["zconf.h","zlib.h","zutil.h"]:
        pisitools.insinto("/usr/include", header)

    pisitools.doman("zlib.3")
    pisitools.dodoc("FAQ", "README", "ChangeLog", "algorithm.txt")

    # absolute path cross compilation fix
    pisitools.dosed("%s/usr/lib/libz.so" % get.installDIR(), "/lib/libz.so", "../../lib/libz.so")

