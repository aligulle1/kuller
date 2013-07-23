#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("docs/Makefile.in", "share/gtk-doc/html/gegl", "share/doc/%s/html" % get.srcTAG())
    autotools.configure("--enable-mmx \
                         --enable-sse \
                         --enable-workshop")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodir("/usr/include/gegl-0.0/gegl/buffer")
    pisitools.dodir("/usr/include/gegl-0.0/gegl/module")

    for header in [h for h in shelltools.ls("gegl/buffer") if h.endswith(".h")]:
        pisitools.insinto("/usr/include/gegl-0.0/gegl/buffer", "gegl/buffer/%s" % header)

    for header in [h for h in shelltools.ls("gegl/module") if h.endswith(".h")]:
        pisitools.insinto("/usr/include/gegl-0.0/gegl/module", "gegl/module/%s" % header)

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "COPYING.LESSER", "NEWS", "README")

