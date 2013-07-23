#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2008  TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "."
NoStrip = "/"

datadir = "/usr/share"

def install():
    pisitools.dodir(datadir)
    shelltools.copytree("playonlinux", "%s/%s/" % (get.installDIR(), datadir))

    pisitools.dobin("playonlinux/playonlinux")

#    pisitools.domo("playonlinux/lang/po/tr.po", "tr", "pol.mo")

#    pisitools.domove("usr/share/locale/tr/LC_MESSAGES", "/usr/share/playonlinux/lang/locale/tr")

    pisitools.dodoc("playonlinux/LICENCE", "playonlinux/CHANGELOG")
