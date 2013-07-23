#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    shelltools.system("qmake-qt4")
    shelltools.cd("qstardict/translations")
    shelltools.system("lrelease-qt4 *.ts")

def build():
    autotools.make()

def install():
    pisitools.dobin("qstardict/qstardict")

    for pixmap in ["qstardict/*.png"]:
        pisitools.insinto("/usr/share/pixmaps", pixmap)
    pisitools.insinto ("/usr/share/applications", "qstardict/qstardict.desktop")
    pisitools.insinto ("/usr/share/qstardict/translations", "qstardict/translations/*.qm")

    pisitools.dolib("plugins/web/libweb.so","usr/lib/qstardict/plugins/")
    pisitools.dolib("plugins/stardict/libstardict.so","usr/lib/qstardict/plugins/")

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "README", "TODO","THANKS")

