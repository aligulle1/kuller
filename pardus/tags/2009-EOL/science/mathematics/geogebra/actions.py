#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools

WorkDir = "GeoGebra.app"


def install():
    pisitools.insinto("/usr/share/geogebra","*")

    pisitools.dosym("/usr/share/geogebra/geogebra.sh", "/usr/bin/geogebra")

    pisitools.dodoc("Contents/Resources/gpl-2.0.txt")
