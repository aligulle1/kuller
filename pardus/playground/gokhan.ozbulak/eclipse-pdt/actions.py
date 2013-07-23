#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2011 TUBITAK/BILGEM
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools

WorkDir = "eclipse-pdt-2.1.2"

def install():
    pisitools.dodir("/opt/eclipse")

    pisitools.insinto("/opt/eclipse", "plugins")
    pisitools.insinto("/opt/eclipse", "features")
