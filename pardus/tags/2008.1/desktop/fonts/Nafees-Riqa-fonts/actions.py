#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools

WorkDir = "."

def install():
    pisitools.insinto("/usr/share/fonts/nafees", "Nafees Riqa v1.0.ttf", "Nafees_Riqa.ttf")
