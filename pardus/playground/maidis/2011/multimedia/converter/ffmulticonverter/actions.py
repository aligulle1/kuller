#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools

WorkDir = "Ilias95-FF-Multi-Converter-416b86f"

def build():
    pythonmodules.compile()

def install():
    pythonmodules.install()

    pisitools.domove("/usr/share/icons/ffmulticonverter.png", "/usr/share/pixmaps")
    pisitools.removeDir("/usr/share/icons")

    pisitools.dodoc("ChangeLog", "COPYING", "README*", "TODO")
