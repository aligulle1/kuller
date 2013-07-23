#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools 

def install():
    pisitools.dolib("commons-io-2.0.jar", "/usr/share/java")
    pisitools.dosym("commons-io-2.0.jar", "/usr/share/java/commons-io.jar")

    pisitools.dohtml("docs/*")
    pisitools.dodoc("LICENSE.txt", "NOTICE.txt", "RELEASE-NOTES.txt")
