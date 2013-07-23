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
    autotools.autoreconf("-fi")
    libtools.libtoolize("--force --install")
    pisitools.dosed("Makefile.in", r"(^program_transform_name\s*=).*", r"\1")

    autotools.configure("--enable-libjpeg \
                         --enable-opengl \
                         --enable-shared \
                         --disable-static")

def build():
    autotools.make()

def install():
    autotools.rawInstall("program_transform_name= DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("NEWS", "README", "doc/*")
