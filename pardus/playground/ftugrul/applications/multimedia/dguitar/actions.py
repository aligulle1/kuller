#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2007  TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.
#
# Fahri Tuğrul Gürkaynak <ftugrul@gmail.com>

from pisi.actionsapi import pisitools

WorkDir="DGuitar-0.5.8"

def install():
    pisitools.insinto("/usr/share/dguitar/", "DGuitar.sh")
    pisitools.insinto("/usr/share/dguitar/dist/", "dist/DGuitar.jar")
    pisitools.insinto("/usr/share/dguitar/dist/", "dist/Common.jar")
    pisitools.insinto("/usr/share/dguitar/lang/", "lang/lang*.*")
    pisitools.insinto("/usr/share/dguitar/skins/", "skins/*.*")
    pisitools.insinto("/usr/share/dguitar/skins/compact/", "skins/compact/*.*")
    pisitools.insinto("/usr/share/dguitar/skins/default/", "skins/default/*.*")
    pisitools.insinto("/usr/share/dguitar/files/", "files/*.*")
    pisitools.insinto("/usr/share/pixmaps", "skins/dguitar_32x32.png", "dguitar.png")
    pisitools.dosym("/usr/share/dguitar/DGuitar.sh", "/usr/bin/dguitar")