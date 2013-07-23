#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools

WorkDir = "xalan-j_2_7_1"

def install():
    pisitools.dodir("/usr/share/java/xalan")

    pisitools.dolib("xalan.jar", "/usr/share/java/xalan")
    pisitools.dolib("serializer.jar", "/usr/share/java/xalan")

    pisitools.dohtml("docs/*")
    pisitools.dodoc("LICENSE.txt", "NOTICE.txt")
