#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    # Static libs should be enabled for mono compiler
    autotools.configure("--with-tls=__thread \
                         --with-jit \
                         --with-ikvm \
                         --with-xen_opt \
                         --enable-static \
                         --with-sigaltstack \
                         --with-libgdiplus=installed")

def build():
    autotools.make("-j1")

def install():
    autotools.install()

    # No static libs
    pisitools.remove("/usr/lib/*.a")

    pisitools.dodoc("AUTHORS", "COPYING.LIB", "ChangeLog", "LICENSE", "NEWS", "README")
