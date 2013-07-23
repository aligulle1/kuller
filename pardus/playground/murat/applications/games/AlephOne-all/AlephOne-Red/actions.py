#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools

WorkDir = "Marathon RED"
datadir = "/usr/share/AlephOne/Red"

def install():
    for dirs in ["Scripts", "Themes"]:
        pisitools.insinto(datadir, dirs)

    for data in ["NET*", "RED*", "Fonts"]:
        pisitools.insinto(datadir, data)
