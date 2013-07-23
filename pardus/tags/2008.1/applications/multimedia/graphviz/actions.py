#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--disable-static \
                         --with-libgd \
                         --with-pangocairo \
                         --with-fontconfig \
                         --disable-dependency-tracking \
                         --disable-php \
                         --disable-ruby \
                         --disable-tcl")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    for lang in ["guile", "io", "java", "lua", "ocaml", "php" , "ruby", "sharp", "tcl"]:
        pisitools.removeDir("/usr/lib/graphviz/%s" % lang)

    pisitools.dohtml(".")
    pisitools.dodoc("AUTHORS", "ChangeLog", "FAQ.txt", "NEWS", "README*")
