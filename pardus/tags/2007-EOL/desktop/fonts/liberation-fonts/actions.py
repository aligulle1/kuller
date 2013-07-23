#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007,2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools

def install():
    pisitools.insinto("/usr/share/fonts/liberation-fonts", "*.ttf")
    pisitools.dosym("../conf.avail/59-liberation-fonts.conf", "/etc/fonts/conf.d/59-liberation-fonts.conf")

    pisitools.dodoc("COPYING", "*.txt")
