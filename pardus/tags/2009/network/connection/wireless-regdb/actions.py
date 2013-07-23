#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools

WorkDir = "wireless-regdb-2009.04.17"
NoStrip = ["/"]

def install():
    pisitools.insinto("/usr/lib/crda", "regulatory.bin")

    pisitools.doman("regulatory.bin.5")
    pisitools.dodoc("README", "LICENSE")
