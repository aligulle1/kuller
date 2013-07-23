#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="ASTranslator"

def setup():
    shelltools.system("qmake-qt4 PREFIX=/usr")

def build():
    autotools.make()

def install():
    pisitools.dobin("bin/Translator")
    pisitools.dosym("/usr/bin/Translator", "/usr/bin/astranslator")

    pisitools.insinto("/usr/share/pixmaps", "src/res/icon.png", "astranslator.png")
    pisitools.insinto("/usr/share/icons/hicolor/128x128/apps", "src/res/icon-128.png", "astranslator.png")

    pisitools.dodoc("*.txt")
