#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools

def install():
    pisitools.dodir("/usr/share/java/xml-commons-external")

    pisitools.dolib("xml-apis.jar", "/usr/share/java/xml-commons-external")
    pisitools.dolib("xml-apis-ext.jar", "/usr/share/java/xml-commons-external")

    pisitools.dohtml("docs/*")
    pisitools.dodoc("KEYS", "LICENSE", "NOTICE", "LICENSE.dom-software.txt", "LICENSE.dom-documentation.txt", "LICENSE.sax.txt", "README.dom.txt", "README.sax.txt")
