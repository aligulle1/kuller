#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    for f in ["NEWS", "AUTHORS"]:
        shelltools.touch(f)

    autotools.autoreconf("-fi")
    autotools.configure("--with-libexif \
                         --with-exiv2")

    pisitools.dosed("Makefile", "/usr/lib/gimp/", "%s/usr/lib/gimp/" % get.installDIR())

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("COPYING", "ChangeLog", "MANIFEST", "README")
