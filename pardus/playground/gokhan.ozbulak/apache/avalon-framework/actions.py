#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools 

WorkDir='.'

def install():
    pisitools.dodir("/usr/share/java/avalon-framework")

    ''' Copying only necessary jar files  '''
    pisitools.dolib("avalon-framework-api-4.3.1.jar", "/usr/share/java/avalon-framework")
    pisitools.dolib("avalon-framework-impl-4.3.1.jar", "/usr/share/java/avalon-framework")
    pisitools.dolib("avalon-logkit-2.2.1.jar", "/usr/share/java/avalon-framework")

    pisitools.dosym("avalon-framework-api-4.3.1.jar", "/usr/share/java/avalon-framework/avalon-framework-api.jar")
    pisitools.dosym("avalon-framework-impl-4.3.1.jar", "/usr/share/java/avalon-framework/avalon-framework-impl.jar")
    pisitools.dosym("avalon-logkit-2.2.1.jar", "/usr/share/java/avalon-framework/avalon-logkit.jar")
