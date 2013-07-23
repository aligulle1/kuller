#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    # Static libs should be enabled for mono compiler
    autotools.configure("--with-tls=__thread \
                         --with-jit=yes \
                         --with-ikvm=yes \
                         --with-xen_opt=yes \
                         --enable-static=yes \
                         --with-sigaltstack=yes \
                         --with-libgdiplus=installed")

def build():
    autotools.make("-j1")

def install():
    autotools.install()
    pisitools.dodoc("AUTHORS", "COPYING.LIB", "ChangeLog", "LICENSE", "NEWS", "README")
