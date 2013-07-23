#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="metaxy-openBibleViewer-0.4.1-0-g64e50c7"

def setup():
    shelltools.system("qmake-qt4 PREFIX=/usr")

def build():
    autotools.make()

def install():
    autotools.install("INSTALL_ROOT=%s" % get.installDIR())

    pisitools.insinto("/usr/share/pixmaps", "src/icons/124x124/openBibleViewer.png")
    pisitools.insinto("/usr/share/icons/hicolor/124x124/apps", "src/icons/124x124/openBibleViewer.png")

    pisitools.dodoc("LICENSE", "README")
