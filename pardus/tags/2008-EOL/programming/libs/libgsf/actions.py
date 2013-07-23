#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    pisitools.dosed("Makefile.*", "gsf-gnome", "")
    pisitools.dosed("Makefile.*", "thumbnailer", "")
    pisitools.dosed("Makefile.*", "doc", "")

    autotools.configure("--disable-static \
                         --without-gnome-vfs \
                         --without-bonobo")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("ChangeLog","NEWS","BUGS","README", "AUTHORS", "TODO", "HACKING", "COPYING")
