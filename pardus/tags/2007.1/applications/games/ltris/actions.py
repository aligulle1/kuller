#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "ltris-1.0.11"

def setup():
    autotools.configure("--localstatedir=/var/games")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.insinto("/usr/share/pixmaps", "icons/ltris48.xpm")
    pisitools.dodoc("TODO", "ChangeLog", "README", "NEWS", "COPYING", "AUTHORS", "INSTALL", "ABOUT-NLS")
