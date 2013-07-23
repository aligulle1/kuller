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
    autotools.autoconf()
    autotools.configure("--disable-dependency-tracking \
                         --enable-optimize \
                         --enable-nls")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.remove("/usr/share/applications/enigma.desktop")

    pisitools.dodoc("NEWS", "README", "AUTHORS", "ChangeLog", "doc/TODO", "doc/CREATING-LEVELS", "doc/HACKING")
    pisitools.dohtml("doc/*")
    pisitools.doman("doc/enigma.6")
