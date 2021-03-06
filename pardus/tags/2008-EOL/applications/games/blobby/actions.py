#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools

def setup():
    cmaketools.configure()

def build():
    cmaketools.make()

def install():
    for bin in ["src/blobby", "src/blobby_server"]:
        pisitools.dobin(bin)

    for data in ["data/backgrounds", "data/gf2x", "data/gfx", "data/sounds", "data/scripts", "data/*.xml"]:
        pisitools.insinto("/usr/share/blobby", data)

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README", "TODO", "doc/*.txt")
