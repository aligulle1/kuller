#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2011 TUBITAK/BILGEM
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

shelltools.export("HOME", get.workDIR())

def build():
    autotools.make()
    pisitools.dosed("src","./images/","/usr/games/frogatto/images/")
    pisitools.dosed("src","data/","/usr/games/frogatto/data/")
    pisitools.dosed("src","music/","/usr/games/frogatto/music/")
    pisitools.dosed("src","music_acc/","/usr/games/frogatto/music_aac/")
    pisitools.dosed("src","sounds/","/usr/games/frogatto/sounds/")
    pisitools.dosed("src","sounds_wav/","/usr/games/frogatto/sounds_wav/")
    pisitools.dosed("src","FreeMono.ttf","/usr/games/frogatto/FreeMono.ttf")

def install():
    pisitools.dobin("game")
    pisitools.insinto("/usr/games/","frogatto-1.1.1")
    pisitools.insinto("/usr/include/frogatto","*.o")
    pisitools.insinto("/usr/include/frogatto","src")
    pisitools.insinto("/usr/include/frogatto","utils")
    pisitools.insinto("/usr/include/frogatto","data")
    pisitools.insinto("/usr/include/frogatto","*.ttf")
    pisitools.insinto("/usr/include/frogatto","*.pl")
    pisitools.insinto("/usr/share/frogatto","*")
    pisitools.dodoc("CHANGELOG","LICENSE")
