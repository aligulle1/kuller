#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="pencil_svn_20090809" 

def setup():
    shelltools.system("qmake-qt4")
    shelltools.cd("src/plugins/imageplugin")
    shelltools.system("qmake-qt4")
    shelltools.cd("../xsheetplugin")
    shelltools.system("qmake-qt4")

def build():
    autotools.make()
    shelltools.cd("src/plugins/imageplugin")
    autotools.make()
    shelltools.cd("../xsheetplugin")
    autotools.make()

def install():
    pisitools.dobin("release/Pencil")

    pisitools.insinto("/usr/share/pixmaps", "icons/pencil.png")

    pisitools.dolib("release/plugins/*", "/usr/lib/pencil/")
    pisitools.dolib("release/libpencil*")

    pisitools.dodoc("LICENSE*", "README", "TODO")
