#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools

WorkDir = "Marathon EVIL"
datadir = "/usr/share/AlephOne/Evil"

def install():
    for dirs in ["Scripts", "Themes"]:
        pisitools.insinto(datadir, dirs)

    for data in ["Cursed*", "Music*", "Fonts"]:
        pisitools.insinto(datadir, data)

    pisitools.dodoc("EVIL ReadMe.txt")
