#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import libtools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.export("CXXFLAGS","%s -fno-strict-aliasing" % get.CXXFLAGS())

    autotools.configure("--without-gnome-print \
                         --without-gnome-vfs \
                         --with-python")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.remove("/usr/share/locale/tr/LC_MESSAGES/inkscape.mo")
    pisitools.domo("tr.po","tr","inkscape.mo")

    pisitools.dodoc("AUTHORS", "TRANSLATORS", "COPYING", "COPYING.LIB", "ChangeLog", "HACKING", "NEWS", "README")

