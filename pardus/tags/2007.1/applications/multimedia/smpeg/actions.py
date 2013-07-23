#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.export("CC", get.CC())
    shelltools.export("CXX", get.CXX())
    shelltools.export("RANLIB", get.RANLIB())
    shelltools.export("AR", get.AR())

    autotools.configure("--with-x \
                         --enable-opengl-player \
                         --disable-gtk-player \
                         --enable-mmx \
                         --enable-debug")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("CHANGES", "README*", "TODO")

