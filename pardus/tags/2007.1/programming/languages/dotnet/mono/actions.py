#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.configure("--with-tls=__thread \
                         --with-jit=yes \
                         --with-ikvm=yes \
                         --with-xen_opt=yes \
                         --enable-static=no \
                         --with-sigaltstack=yes \
                         --with-libgdiplus=installed")

def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.dodoc("AUTHORS", "COPYING.LIB", "ChangeLog", "LICENSE", "NEWS", "README")
