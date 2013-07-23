#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools

def install():
    pisitools.dolib("build/xmlgraphics-commons-1.4.jar", "/usr/share/java")
    pisitools.dosym("xmlgraphics-commons-1.4.jar", "/usr/share/java/xmlgraphics-commons.jar")

    pisitools.dohtml("docs/*")
    pisitools.dodoc("KEYS", "LICENSE", "NOTICE", "README")
