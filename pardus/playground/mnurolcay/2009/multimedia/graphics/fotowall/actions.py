#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="Fotowall-%s" % get.srcVERSION()

def setup():
    shelltools.system("qmake-qt4")

def build():
    autotools.make()

def install():
    autotools.rawInstall("INSTALL_ROOT=%s" % get.installDIR())

    shelltools.system("lrelease-qt4 fotowall.pro")
    pisitools.insinto("/usr/share/fotowall/i18n/", "translations/*.qm")

    pisitools.dodoc("GPL_V2", "3rdparty/posterazor/GPL_V3", "README*")
