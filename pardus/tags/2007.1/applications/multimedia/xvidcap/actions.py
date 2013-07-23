#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "xvidcap-1.1.3-20060423"

def setup():
    autotools.configure("--with-gtk2 --with-forced-embedded-ffmpeg")

def build():
    autotools.make("gvidcap")

def install():
    pisitools.dobin("src/gvidcap")
    pisitools.newman("man/gvidcap.man", "gvidcap.1")
    pisitools.insinto("/usr/share/pixmaps", "xbm/select.png", "gvidcap.png")
    pisitools.dodoc("NEWS", "TODO", "README", "AUTHORS", "ChangeLog", "XVidcap.ad")
