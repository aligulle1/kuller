#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def install():
    pisitools.dobin("bin/blogtk2")

    pisitools.insinto("/usr/share/blogtk2/lib/blogtk2/", "share/blogtk2/lib/blogtk2/*")
    pisitools.insinto("/usr/share/blogtk2/glade", "share/blogtk2/glade/*.glade")
    pisitools.insinto("/usr/share/blogtk2/res", "share/blogtk2/res/*.png")
    pisitools.insinto("/usr/share/pixmaps", "data/blogtk-icon.png", "blogtk.png")
    pisitools.insinto("/usr/share/applications", "data/blogtk.desktop")

    pisitools.dodoc("ChangeLog", "AUTHORS", "README")
