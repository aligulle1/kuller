#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools 

def install():
    pisitools.dodir("/usr/share/java/commons-logging")

    ''' Copying only necessary jar files  '''
    pisitools.dolib("commons-logging-1.1.1.jar", "/usr/share/java/commons-logging")
    pisitools.dolib("commons-logging-adapters-1.1.1.jar", "/usr/share/java/commons-logging")
    pisitools.dolib("commons-logging-api-1.1.1.jar", "/usr/share/java/commons-logging")

    pisitools.dosym("commons-logging-1.1.1.jar", "/usr/share/java/commons-logging/commons-logging.jar")
    pisitools.dosym("commons-logging-adapters-1.1.1.jar", "/usr/share/java/commons-logging/commons-logging-adapters.jar")
    pisitools.dosym("commons-logging-api-1.1.1.jar", "/usr/share/java/commons-logging/commons-logging-api.jar")

    pisitools.dohtml("site/*")
    pisitools.dodoc("LICENSE.txt", "NOTICE.txt", "RELEASE-NOTES.txt")
