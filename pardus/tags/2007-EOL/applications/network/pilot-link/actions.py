#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import perlmodules
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get

def setup():
    autotools.configure("--disable-debug \
                         --enable-static=no \
                         --includedir=/usr/include/libpisock \
                         --with-java=no \
                         --with-perl=yes \
                         --with-python=yes \
                         --with-libpng=/usr \
                         --with-readline=yes \
                         --with-bluez \
                         --enable-conduits \
                         --enable-threads \
                         --enable-libusb")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    perlmodules.fixLocalPod()
    pythonmodules.fixCompiledPy()

    pisitools.dodoc("ChangeLog", "README", "doc/README*", "doc/TODO", "NEWS", "AUTHORS")
