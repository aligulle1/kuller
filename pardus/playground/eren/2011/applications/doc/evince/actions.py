#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2005  TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.configure("--enable-static=no \
                         --disable-scrollkeeper \
                         --enable-pdf \
                         --enable-tiff \
                         --enable-djvu \
                         --enable-dvi \
                         --enable-t1lib \
                         --enable-pixbuf \
                         --with-libgnome \
                         --with-print=gnome")



def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("README", "TODO", "AUTHORS", "ChangeLog")
    pisitools.remove("/usr/share/icons/hicolor/icon-theme.cache")
