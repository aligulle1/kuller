#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010-2011 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

shelltools.export("HOME", get.workDIR())

def setup():
    options = "--disable-static \
               --enable-silent-rules \
               --enable-introspection \
               --with-libjasper \
               --with-included-loaders=png"

    if get.buildTYPE() == "emul32":
        options += " --prefix=/emul32 \
                     --libdir=/usr/lib32"
        shelltools.export("CFLAGS", "%s -m32" % get.CFLAGS())

    autotools.autoreconf("-fiv")

    autotools.configure(options)

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    if get.buildTYPE() == "emul32":
        pisitools.domove("/emul32/bin/gdk-pixbuf-query-loaders", "/usr/bin", "gdk-pixbuf-query-loaders-32bit")
        pisitools.removeDir("/emul32")

    #if get.buildTYPE() == "emul32":
    #    pisitools.remove("/usr/lib32/gdk-pixbuf-2.0/2.10.0/loaders.cache")
    #else:
    #    pisitools.remove("/usr/lib/gdk-pixbuf-2.0/2.10.0/loaders.cache")

    pisitools.dodoc("AUTHORS", "COPYING", "NEWS", "README")
