#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools

WorkDir="oxygen"

def install():
    pisitools.insinto("/usr/share/qmmp/skins/oxygen", "*")

    pisitools.dodoc("readme.txt")
