#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import crosstools as autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

arch = get.ARCH()
if arch.startswith("arm"):
    optimizationtype = ""
else:
    optimizationtype = "--enable-amd64" if arch == "x86_64" else "--enable-mmx"

def setup():
    autotools.environment["optimizationtype"] = optimizationtype
    autotools.configure("--disable-static \
                         --with-x \
                         --with-jpeg \
                         --with-png \
                         --with-tiff \
                         --with-gif \
                         --with-zlib \
                         --with-bzip2 \
                         --with-id3 \
                         --enable-visibility-hiding \
                         --x-includes=%(SysRoot)s/usr/include \
                         --x-libraries=%(SysRoot)s/usr/lib \
                         --with-gnu-ld \
                         %(optimizationtype)s" % autotools.environment)

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dohtml("doc/*")
    pisitools.dodoc("AUTHORS", "ChangeLog", "README", "TODO")
