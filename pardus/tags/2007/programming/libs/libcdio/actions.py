#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005,2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import libtools


def setup():
    libtools.libtoolize("--copy --force")
    autotools.configure("--enable-static=no \
                         --with-cd-paranoia-name=libcdio-paranoia \
                         --disable-vcd-info \
                         --disable-dependency-tracking \
                         --disable-cddb")

def build():
    autotools.make("-j1")

def install():
    autotools.rawInstall("DESTDIR=%s" % (get.installDIR()))

    pisitools.dodoc("AUTHORS", "ChangeLog", "INSTALL", "NEWS", "README", "THANKS")
