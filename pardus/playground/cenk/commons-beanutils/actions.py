#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="commons-beanutils-%s-src" % get.srcVERSION()

def setup():
    for jars in ["build.properties", "optional/bean-collections/build.properties"]:
        pisitools.echo("%s" % jars, "commons-collections.jar=/usr/share/java/commons-collections.jar")
        pisitools.echo("%s" % jars, "commons-logging.jar=/usr/share/java/commons-logging.jar")

def build():
    shelltools.system("ant dist")

def install():
    pisitools.insinto("/usr/share/java","dist/*.jar")

    pisitools.dohtml("*.html")
    pisitools.dodoc("README.txt", "LICENSE.txt", "NOTICE.txt", "RELEASE-NOTES.txt")
