#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir="XaraLX-0.7r1764"

def setup():
    shelltools.system("./autogen.sh")
    autotools.configure()

def build():
    autotools.make()

def install():
    pisitools.dobin("XaraLX")
    pisitools.dosym("/usr/bin/XaraLX", "/usr/bin/xaralx")
    pisitools.insinto("/usr/share/applications", "xaralx.desktop")
    pisitools.insinto("/usr/share/pixmaps", "xaralx.xpm")
    pisitools.dodoc("ABOUT-NLS", "LICENSE", "README", "Designs/*", "TextDesigns/*", )
