#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

version_underscore = "1_35"
version = get.srcVERSION()

WorkDir="boost_1_35_0"

def setup():
    pisitools.dosed("tools/build/v2/tools/gcc.jam", "PARDUS_FLAGS", get.CFLAGS())

    autotools.rawConfigure("--prefix=%s/usr \
                            --with-icu=/usr" % get.installDIR())

def build():
    autotools.make()

def install():
    autotools.install()

    # Remove duplicate/unneeded libraries
    pisitools.remove("/usr/lib/*.a")
    pisitools.remove("/usr/lib/*.so")
    pisitools.remove("/usr/lib/*-d*")
    pisitools.remove("/usr/lib/*-gcc43-1*")

    # Create symlinks
    libraries = shelltools.ls("%s/usr/lib/" % get.installDIR())
    for lib in libraries:
        fixedName = lib.replace("-gcc43-mt-%s.so.%s" % (version_underscore,version), "")
        pisitools.dosym("%s" % lib, "/usr/lib/%s.so" % fixedName)

    pisitools.insinto("/usr/include","%s/usr/include/boost-%s/boost" % (get.installDIR(),version_underscore))
    pisitools.removeDir("/usr/include/boost-%s" % version_underscore)

    pisitools.dohtml("doc/html/*")
    pisitools.dodoc("README*")
