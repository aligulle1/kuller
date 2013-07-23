#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    autotools.configure("--x-includes=/usr/include/X11/ \
                         --x-libraries=/usr/include/X11/")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.insinto("/usr/share/pixmaps", "cgoban_icon.png", "cgoban.png")

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README", "TODO")
