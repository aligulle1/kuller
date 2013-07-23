#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "videocut-%s.orig" % get.srcVERSION()

def setup():
    shelltools.system("qmake-qt4 videocut.pro")

def build():
    autotools.make()

def install():
    pisitools.dobin("build/result/videocut")
    pisitools.insinto("/usr/share/applications", "videocut.desktop")
    pisitools.insinto("/usr/share/icons", "videocut.svg")

    pisitools.dodoc("LICENSE", "THANKSTO", "AUTHORS")
