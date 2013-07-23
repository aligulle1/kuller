#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.system("qmake-qt4 PREFIX=/usr")

def build():
    autotools.make()

def install():
    autotools.rawInstall("INSTALL_ROOT=%s" % get.installDIR())

    # Don't know, why package manager can't show the icon when there is a .svg
    #pisitools.remove("/usr/share/icons/hicolor/scalable/apps/arora.svg")

    pisitools.dodoc("AUTHORS", "README", "ChangeLog", "LICENSE*")
