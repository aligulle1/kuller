#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#

from pisi.actionsapi import pisitools

WorkDir = "Chromium-0.9/data"
destinationDIR = "/usr/share/chromium/data/"

def install():
    pisitools.insinto(destinationDIR + "wav", "wav/*.wav")
    pisitools.insinto(destinationDIR + "png", "png/*.png")
    pisitools.insinto(destinationDIR + "png", "png/*.jpg")
    pisitools.insinto(destinationDIR + "fonts", "fonts/space.*")
    pisitools.insinto(destinationDIR + "doc", "doc/*.htm")
    pisitools.insinto(destinationDIR + "doc/images", "doc/images/*.jpg")
