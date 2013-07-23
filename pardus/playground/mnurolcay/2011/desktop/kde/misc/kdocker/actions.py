#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import qt4
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    qt4.configure()

def build():
    qt4.make()

def install():
    qt4.install()

    pisitools.dosym("/usr/share/kdocker/icons/kdocker.png", "/usr/share/pixmaps/kdocker.png")

    pisitools.dodoc("AUTHORS", "BUGS", "ChangeLog", "COPYING", "CREDITS", "README", "TODO")
