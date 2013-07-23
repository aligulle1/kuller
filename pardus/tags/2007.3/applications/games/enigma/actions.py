#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2007 TUBITAK/UEKAE
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

    # we will use our desktop file
    pisitools.remove("/usr/share/applications/enigma.desktop")

    # we don't need enet devel stuff
    pisitools.removeDir("/usr/include")
    pisitools.removeDir("/usr/lib")

    pisitools.dodoc("ACKNOWLEDGEMENTS", "AUTHORS", "CHANGES", "README", "doc/HACKING")
    pisitools.dohtml("doc/*")
    pisitools.doman("doc/enigma.6")
