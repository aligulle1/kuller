#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools

WorkDir = "."
NoStrip = "/"

def install():
    shelltools.system("sh etf_1.6-english-2.run --noexec --keep --target enemy-territory-fortress-1.6")
    shelltools.cd("enemy-territory-fortress-1.6")
    shelltools.system("tar -zxvf etf.tar.gz")
    pisitools.insinto("/usr/share/pixmaps/", "etf.xpm")
    pisitools.insinto("/opt/enemy-territory/", "omnibot_etf.so")
    pisitools.insinto("/opt/enemy-territory/etf", "etf/*")
    pisitools.insinto("/opt/enemy-territory/", "bin/et-f")
    pisitools.dodoc("LICENSE", "README", "README.etf", "etf/ChangeLog", "etf/LICENSE", "cfghi.tar.gz", "cfglow.tar.gz", "cfgnormal.tar.gz", "cfgxtrahi.tar.gz")
    pisitools.dohtml("etf/docs/")
