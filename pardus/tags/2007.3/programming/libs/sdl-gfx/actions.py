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

WorkDir = "SDL_gfx-%s" % get.srcVERSION()

def setup():
    autotools.configure("--enable-mmx \
                         --disable-static")

def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.dodoc("AUTHORS", "ChangeLog", "LICENSE", "README")
    shelltools.copytree("Docs", "%s/%s/%s/html" % (get.installDIR(), get.docDIR(), get.srcTAG()))
