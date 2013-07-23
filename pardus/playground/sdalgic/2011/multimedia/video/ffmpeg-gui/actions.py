#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import qt4

WorkDir = "ffmpeg-gui"
# NoStrip = "/"

def setup():
    qt4.configure()

def build():
    qt4.make()

def install():
    pisitools.dobin("ffmpeg-gui")

    pisitools.insinto("/usr/share/applications", "ffmpeg-gui.desktop")
    pisitools.insinto("/usr/share/qt4/translations/", "translations/*.qm")
    pisitools.insinto("/usr/share/pixmaps", "icons/icon128.png", "ffmpeg-gui.png")

    pisitools.dodoc("COPYING", "README*")
