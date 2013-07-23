#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

version = get.srcVERSION()
version_underscore, patch_release = version.replace(".", "_").rsplit("_", 1)

WorkDir = "boost_%s_%s" % (version_underscore, patch_release)

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

    # FIXME: Really fix library names
    # Create symlinks
    libraries = shelltools.ls("%s/usr/lib/" % get.installDIR())
    for lib in libraries:
        fixedName = lib.replace("-gcc43-mt-%s.so.%s" % (version_underscore, version), "")
        pisitools.dosym(lib, "/usr/lib/%s.so" % fixedName)
        pisitools.dosym(lib, "/usr/lib/%s-mt.so" % fixedName)

    pisitools.domove("/usr/include/boost-*/boost", "/usr/include")
    pisitools.removeDir("/usr/include/boost-*")

    pisitools.dohtml("doc/html/*")
    pisitools.dodoc("LICENSE*")
