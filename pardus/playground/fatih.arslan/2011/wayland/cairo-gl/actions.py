#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    # We need to create initial Makefiles, the archive is created from git
    shelltools.system("./autogen.sh")

    autotools.autoreconf("-vif")
    autotools.configure("--disable-static \
                         --disable-gtk-doc \
                         --enable-glitz \
                         --enable-xlib \
                         --enable-xlib-xrender \
                         --enable-gl \
                         --enable-egl \
                         --enable-xcb \
                         --enable-ft \
                         --enable-ps \
                         --enable-pdf \
                         --enable-svg \
                         --enable-tee \
                         --enable-png \
                         --with-x")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "README", "ChangeLog", "NEWS", "COPYING", "COPYING-LGPL-2.1", "COPYING-MPL-1.1")
