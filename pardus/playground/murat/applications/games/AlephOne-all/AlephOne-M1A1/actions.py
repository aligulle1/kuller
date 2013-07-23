#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools

datadir = "/usr/share/AlephOne/Marathon1"

def install():
    pisitools.insinto(datadir, "M1A1*")

    for data in ["MML","Tracks"]:
        pisitools.insinto(datadir, data)

    pisitools.dodoc("Aleph One Log.txt", "Marathon_Manual.pdf")
    pisitools.dohtml("ReadMe_M1A1_SDL.html")
