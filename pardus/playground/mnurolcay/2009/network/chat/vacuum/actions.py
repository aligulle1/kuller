#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    shelltools.system("qmake-qt4 INSTALL_PREFIX=/usr")

def build():
    autotools.make()

def install():
    autotools.rawInstall("INSTALL_ROOT=%s" % get.installDIR())

    pisitools.insinto("/usr/share/applications", "src/packages/linux/vacuum.desktop")

    pisitools.dodoc("AUTHORS", "CHANGELOG", "COPYING", "README")
