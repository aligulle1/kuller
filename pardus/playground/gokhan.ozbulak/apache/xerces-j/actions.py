#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools

WorkDir = "xerces-2_10_0"

def install():
    pisitools.dodir("/usr/share/java/xerces")

    pisitools.dolib("xercesImpl.jar", "/usr/share/java/xerces")
    pisitools.dolib("resolver.jar", "/usr/share/java/xerces")

    pisitools.dohtml("docs/*")
    pisitools.dodoc("LICENSE", "NOTICE")
