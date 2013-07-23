#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt
 
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir = "peditor"

def setup():
    shelltools.system("qmake-qt4 peditor.pro")

def build():
    autotools.make()

def install():
    pisitools.dobin("bin/peditor")
    pisitools.domove("/usr/bin/peditor", "/usr/bin", "deveditor")

    pisitools.insinto("/usr/share/peditor/doc","doc/")
    pisitools.insinto("/usr/share/peditor/templates","templates/")
    pisitools.insinto("/usr/share/peditor/src","src/")

    pisitools.removeDir("/usr/share/peditor/doc/doc/.svn")
    pisitools.removeDir("/usr/share/peditor/src/src/.svn")
    pisitools.removeDir("/usr/share/peditor/src/src/Blank.template/.svn")
    pisitools.removeDir("/usr/share/peditor/src/src/Standard C++.template/.svn")
    pisitools.removeDir("/usr/share/peditor/src/src/Standard C.template/.svn/")
    pisitools.removeDir("/usr/share/peditor/templates/templates/.svn")

    pisitools.dodoc("AUTHORS", "COPYING")
