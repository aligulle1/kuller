#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005, 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "."

def setup():
    shelltools.system("%s/build -os linux -ws gtk -arch x86" % WorkDir)
    #patch eclipse executable build file
    shelltools.system("ant -f features/org.eclipse.equinox.executable/build.xml");

def install():
    pisitools.dodir("/opt/eclipse")
    shelltools.copytree("eclipse", "%s/opt/eclipse" % get.installDIR())
    #copy eclipse executable
    shelltools.copy("features/org.eclipse.equinox.executable/eclipse", "opt/eclipse/eclipse")
