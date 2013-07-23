#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2011 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

shelltools.export("HOME", get.workDIR())

def setup():
    options = "--disable-static"

    if get.buildTYPE() == "emul32":
#        options += " --prefix=/emul32 \
#                     --libdir=/usr/lib32 \
#                     --libexecdir=/emul32/lib \
#                     --bindir=/emul32/bin \
#                     --sbindir=/emul32/sbin \
#                     --mandir=/emul32/usr/share/man"
        options += " --prefix=/emul32 \
                     --libdir=/usr/lib32"

        shelltools.export("CC", "%s -m32" % get.CC())
        shelltools.export("CFLAGS", "%s -m32" % get.CFLAGS())
        shelltools.export("CXXFLAGS", "%s -m32" % get.CXXFLAGS())
        shelltools.export("LDFLAGS", "%s -m32" % get.LDFLAGS())

    autotools.autoreconf("-fiv")
    autotools.configure(options)

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog*", "COPYING", "README", "NEWS")

    if get.buildTYPE() == "emul32":
        pisitools.domove("/emul32/bin/pango-querymodules", "/usr/bin", "pango-querymodules-32bit")
        pisitools.removeDir("/emul32")
        return
