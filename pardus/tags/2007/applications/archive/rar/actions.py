#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools

WorkDir = "rar"

def install():
    pisitools.insinto("/opt/rar/bin", "rar")
    pisitools.insinto("/opt/rar/lib", "default.sfx")
    pisitools.insinto("/opt/rar/etc", "rarfiles.lst")

    pisitools.dosym("/opt/rar/bin/rar", "/usr/bin/rar")

    pisitools.dodoc("*.txt", "*.diz")